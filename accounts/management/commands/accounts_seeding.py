from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Add new Accounts to the database"

    def handle(self, *args, **options):
        from users.models import Users
        from accounts.models import Accounts

        # delete all accounts
        # Accounts.objects.all().delete()

        # bulk create accounts
        Accounts.objects.bulk_create(
            [
                Accounts(
                    user=Users.objects.get(email="user1@test.com"),
                    paid=79000,
                    memo="dinner",
                ),
                Accounts(
                    user=Users.objects.get(email="user1@test.com"),
                    paid=2500,
                    memo="something i need",
                ),
                Accounts(
                    user=Users.objects.get(email="user1@test.com"),
                    paid=35000,
                    memo="present",
                ),
                Accounts(
                    user=Users.objects.get(email="user1@test.com"),
                    paid=78000,
                    memo="lunch",
                ),
                Accounts(
                    user=Users.objects.get(email="user1@test.com"),
                    paid=12000,
                    memo="dinner",
                ),
                Accounts(
                    user=Users.objects.get(email="user2@test.com"),
                    paid=21000,
                    memo="for my friend",
                ),
                Accounts(
                    user=Users.objects.get(email="user2@test.com"),
                    paid=1200,
                    memo="train",
                ),
                Accounts(
                    user=Users.objects.get(email="user2@test.com"),
                    paid=350000,
                    memo="monthly rent pay",
                ),
                Accounts(
                    user=Users.objects.get(email="user2@test.com"),
                    paid=29000,
                    memo="groceries Shopping",
                ),
                Accounts(
                    user=Users.objects.get(email="user2@test.com"),
                    paid=10000,
                    memo="dinner",
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Successfully generated Accounts!"))
