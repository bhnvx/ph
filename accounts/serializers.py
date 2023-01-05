from rest_framework import serializers

from .models import Accounts


class AccountSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    paid = serializers.IntegerField()
    memo = serializers.CharField()


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['pk', 'paid', 'memo', 'created_at', ]
