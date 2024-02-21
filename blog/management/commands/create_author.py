from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from blog.models import Author


class Command(BaseCommand):
    help = "Create author"

    def handle(self, *args, **kwargs):
        author = Author(
            first_name='Alex',
            last_name='Brown',
            email='ab@gmail.com',
            bio=lorem_ipsum.paragraph(),
            birth_date='1988-12-12'
        )
        author.save()
        self.stdout.write(f'{author}')
