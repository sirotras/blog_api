# posts/management/commands/del_all_posts.py
from django.core.management.base import BaseCommand

from ...models import Post


class Command(BaseCommand):
    help = 'Deletes all posts'
    
    def handle(self, *args, **kwargs):
        Post.objects.all().delete()