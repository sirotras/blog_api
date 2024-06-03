# posts/management/commands/create_posts.py
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import random

from .words import get_word
from ...models import Post


class Command(BaseCommand):
    help = 'Create n amount of posts'
    
    def add_arguments(self,parser):
        parser.add_argument('n', type=int, help='Indicates the number of posts to be created')
    
    def handle(self, *args, **kwargs):
        n = kwargs['n']        
        authors = get_user_model().objects.all()
        
        for i in range(n):
            author = random.choice(authors)
            title = get_word()
            for j in range(random.randint(1,6)):
                title = title + " " + get_word()
            body = get_word()
            for k in range(random.randint(11,33)):
                body = body + " " + get_word()
            #print("{0}\n{1}\n{2}\n".format(author,title,body))   
            Post.objects.create(
                author=author,
                title=title,
                body=body,
            )
        