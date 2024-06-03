# accounts/management/commands/create_users.py
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create 1 admin and n users'
    
    def add_arguments(self,parser):
        parser.add_argument('n', type=int, help='Indicates the number of users to be created')
        
    def handle(self, *args, **kwargs):
        n = kwargs['n']
        #admin create
        admin = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="testpass123",
        )
        
        for i in range(n):
            username = get_random_string(length=5)
            user = get_user_model().objects.create_user(
                username=username,
                email=username+"@email.com",
                password="testpass123",
            )