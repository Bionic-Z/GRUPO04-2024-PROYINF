from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Genera usuarios de prueba aleatorios y los asigna a grupos reader/editor/admin"

    def add_arguments(self, parser):
        parser.add_argument(
            '--count', '-c',
            type=int,
            default=10,
            help='Número de usuarios a crear'
        )

    def handle(self, *args, **options):
        faker = Faker()
        total = options['count']
        roles = list(Group.objects.filter(name__in=['reader','editor','admin']))
        if not roles:
            self.stdout.write(self.style.ERROR(
                "No existen los grupos reader/editor/admin. Ejecuta primero create_roles"
            ))
            return

        for i in range(total):
            username = faker.unique.user_name()
            email = faker.unique.email()
            user = User.objects.create_user(
                username=username,
                email=email,
                password=username
            )
            group = random.choice(roles)
            user.groups.add(group)
            self.stdout.write(
                self.style.SUCCESS(f'[{i+1}/{total}] Usuario {username} ({email}) → {group.name}')
            )

        self.stdout.write(self.style.SUCCESS(f'Seeding completado: {total} usuarios creados.'))
