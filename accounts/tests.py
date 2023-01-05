from test_plus.test import TestCase

from users.models import Users
from .models import Accounts


class AccountTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.user1 = Users.objects.create_user(email="user1@test.com", password="qwer1234", is_active=True)
        self.user2 = Users.objects.create_user(email="user2@test.com", password="qwer1234", is_active=True)

        self.account1 = Accounts.objects.create(user=self.user1, paid=79000, memo="user1_test")
        self.account2 = Accounts.objects.create(user=self.user2, paid=54000, memo="user2_test")

    def user_login(self, instance):
        data = {
            "email": instance.email,
            "password": "qwer1234",
        }

        self.client.post(
            path="/api/v1/users/login/",
            data=data,
            follow=True
        )

    def test_account_create(self):
        # Failed (Not Login)
        data = {
            "paid": 32000,
            "memo": "dinner",
        }

        res = self.client.post(
            path="/api/v1/accounts/",
            data=data
        )
        self.assertEqual(res.status_code, 401)

        # Success
        self.user_login(self.user1)

        res = self.client.post(
            path="/api/v1/accounts/",
            data=data,
        )
        self.assertEqual(res.status_code, 201)

    def test_get_accounts(self):
        self.user_login(self.user1)

        res = self.client.get(
            path="/api/v1/accounts/",
        )
        self.assertEqual(res.status_code, 200)

        return res.json()

    def test_update_accounts(self):
        # Success
        data = {
            "paid": "35000",
            "memo": "account_update_test",
        }

        res = self.client.patch(
            path=f"/api/v1/accounts/{self.test_get_accounts()[0].get('pk')}/",
            data=data,
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)

        # Failed (Another User Account)
        res = self.client.patch(
            path="/api/v1/accounts/2/",
            data=data,
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 404)

    def test_destroy_accounts(self):
        # Success
        res = self.client.delete(
            path=f"/api/v1/accounts/{self.test_get_accounts()[0].get('pk')}/",
        )
        self.assertEqual(res.status_code, 204)

        # Failed (Another User Account)
        res = self.client.delete(
            path="/api/v1/accounts/2/",
        )
        self.assertEqual(res.status_code, 404)
