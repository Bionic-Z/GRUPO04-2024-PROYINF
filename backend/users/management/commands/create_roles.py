from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Crea los grupos de roles básicos (admin, editor, reader)"

    def handle(self, *args, **kwargs):
        roles = ['admin', 'editor', 'reader']
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created rol: {role}'))
            else:
                self.stdout.write(self.style.WARNING(f'Already created: {role}'))
