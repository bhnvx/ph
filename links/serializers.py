from rest_framework import serializers

from .models import Links


class LinkSerializer(serializers.ModelSerializer):
    origin_link = serializers.URLField(required=False)
    encode_link = serializers.URLField(required=False)

    class Meta:
        model = Links
        fields = "__all__"
