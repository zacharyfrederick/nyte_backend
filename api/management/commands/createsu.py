from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import NyteUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not NyteUser.objects.filter(email="zachfred62@gmail.com").exists():
            NyteUser.objects.create_superuser(email="zachfred62@gmail.com", password="HelloEd12")

        if not NyteUser.objects.filter(email="josh@langinc.com").exists():
            NyteUser.objects.create_superuser(email="josh@langinc.com", password="Hughsucksfarts")
        
        if not NyteUser.objects.filter(email="kyle@getnyte.com").exists():
            NyteUser.objects.create_superuser(email="kyle@getnyte.com", password="Nyte123!")
