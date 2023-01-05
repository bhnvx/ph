from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Add new Users to the database"

    def handle(self, *args, **options):
        from users.models import Users
        from django.contrib.auth.hashers import make_password

        # delete all users
        # Users.objects.all().delete()

        # bulk create users
        Users.objects.bulk_create(
            [
                Users(
                    email="admin@help.com",
                    password=make_password("qwer1234"),
                    is_staff=True,
                    is_superuser=True,
                ),
                Users(
                    email="user1@test.com",
                    password=make_password("qwer1234"),
                ),
                Users(
                    email="user2@test.com",
                    password=make_password("qwer1234"),
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Successfully generated Users!"))
