from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin1@mail.ru',
            phone='1112',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('5682')
        user.save()
