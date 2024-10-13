from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create an initial user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='siaforce').exists():
            User.objects.create_user(
                username='siaforce',
                password='siaforce',
                email='user@siaforce.net'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created initial user: siaforce'))
        else:
            self.stdout.write(self.style.WARNING('Initial user already exists'))
