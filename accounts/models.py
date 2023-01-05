from django.db import models

from users.models import Users


class Accounts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    paid = models.IntegerField()
    memo = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"When {self.created_at}, {self.paid} won paid, {self.memo}"

    class Meta:
        db_table = "accounts"
