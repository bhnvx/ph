from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import AccountSerializer, AccountDetailSerializer
from .models import Accounts


class AccountView(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ['get', 'post', 'patch', 'delete', ]

    def get_queryset(self):
        return Accounts.objects.filter(user=self.request.user)

    def perform_create(self, serializer: AccountSerializer):
        Accounts.objects.create(user=self.request.user, **serializer.validated_data)

    def perform_update(self, serializer: AccountSerializer):
        Accounts.objects.filter(pk=self.kwargs['pk']).update(**serializer.validated_data)

    def perform_destroy(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs) -> Response:
        return super(AccountView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs) -> Response:
        self.serializer_class = AccountDetailSerializer
        return super(AccountView, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs) -> Response:
        return super(AccountView, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs) -> Response:
        return super(AccountView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs) -> None:
        return super(AccountView, self).destroy(request, *args, **kwargs)
