from django.db import models

from accounts.models import Accounts


class Links(models.Model):
    accounts = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=False)
    origin_link = models.URLField(max_length=200)
    encode_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expire = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.origin_link} >> {self.encode_link}, it will be expire 30 min later."

    class Meta:
        db_table = "links"
