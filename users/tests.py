from test_plus.test import TestCase

from users.models import Users


class UserTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.user1 = Users.objects.create_user(email="user1@test.com", password="qwer1234", is_active=True)
        self.user2 = Users.objects.create_user(email="user2@test.com", password="qwer1234", is_active=False)

    def test_create_user_case(self):
        # Success
        data = {
            "email": "user3@test.com",
            "password": "qwer1234",
        }

        res = self.client.post(
            path="/api/v1/users/",
            data=data
        )
        self.assertEqual(res.status_code, 201)

        # Failed (already exists)
        res = self.client.post(
            path="/api/v1/users/",
            data=data
        )
        self.assertEqual(res.status_code, 409)

    def test_login_user_case(self):
        # Success
        data = {
            "email": "user1@test.com",
            "password": "qwer1234",
        }

        res = self.client.post(
            path="/api/v1/users/login/",
            data=data,
        )
        self.assertEqual(res.status_code, 200)

        # Failed (Wrong Password)
        data['password'] = "wordpswrd"
        res = self.client.post(
            path="/api/v1/users/login/",
            data=data,
        )
        self.assertEqual(res.status_code, 401)

        # Failed (Not Active User)
        data = {
            "email": "user2@test.com",
            "password": "qwer1234",
        }

        res = self.client.post(
            path="/api/v1/users/login/",
            data=data,
        )
        self.assertEqual(res.status_code, 401)
