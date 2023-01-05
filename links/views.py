import random
import string
from datetime import datetime

from django.conf import settings
from rest_framework import mixins, permissions, exceptions, response, status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import GenericViewSet

from accounts.models import Accounts
from .models import Links
from .serializers import LinkSerializer


class LinkView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer: LinkSerializer):
        _id = serializer.validated_data['accounts']
        base_uri = settings.BASE_URI
        account = Accounts.objects.filter(id=_id.id, user=self.request.user)
        if account:
            encode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            Links.objects.create(
                accounts=account.first(),
                origin_link=f"{base_uri}/api/v1/accounts/{_id.id}/",
                encode_link=f"{base_uri}/{encode}",
            )
            serializer.save(
                origin_link=f"{base_uri}/api/v1/accounts/{_id.id}/",
                encode_link=f"{base_uri}/{encode}"
            )
        else:
            raise exceptions.PermissionDenied('Not Your Accounts.')


@api_view(("GET", ))
@renderer_classes((JSONRenderer, ))
def redirect_origin(request, encode_link) -> response.Response:
    link = Links.objects.filter(encode_link=f"{settings.BASE_URI}/{encode_link}").first()
    if link:
        remain_time = datetime.timestamp(datetime.now()) - datetime.timestamp(link.created_at)
        if remain_time >= 1800:
            link.expire = True
            link.save()
            return response.Response({"message": "Expired Link."}, status=status.HTTP_400_BAD_REQUEST)
        if remain_time < 1800:
            data = Accounts.objects.get(id=link.accounts_id)
            return response.Response({"message": str(data)}, status=status.HTTP_200_OK)
