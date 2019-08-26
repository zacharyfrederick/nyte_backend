from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import NyteUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not NyteUser.objects.filter(email="zachfred62@gmail.com").exists():
            NyteUser.objects.create_superuser(email="zachfred62@gmail.com", password="HelloEd12")
