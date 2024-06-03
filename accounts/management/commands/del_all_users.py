# posts/management/commands/del_all_posts.py
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from ...models import Post


class Command(BaseCommand):
    help = 'Deletes all users'
    
    def handle(self, *args, **kwargs):
        get_user_model().objects.all().delete()