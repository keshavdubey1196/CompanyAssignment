from django.core.management.base import BaseCommand
from base.models import User, Hackathon


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Hackathon.objects.all().delete()
        User.objects.all().delete()

