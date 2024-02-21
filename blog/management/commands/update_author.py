from django.core.management.base import BaseCommand

from blog.models import Author


class Command(BaseCommand):
    help = "Update author by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('first_name', type=str, help='Author first_name')
        parser.add_argument('last_name', type=str, help='Author last_name')
        parser.add_argument('email', type=str, help='Author email')
        parser.add_argument('birth_date', type=str, help='Author birth_date (YYYY-MM-DD)')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        email = kwargs.get('email')
        birth_date = kwargs.get('birth_date')
        author = Author.objects.filter(pk=pk).first()
        author.first_name = first_name
        author.last_name = last_name
        author.email = email
        author.birth_date = birth_date
        author.save()
        self.stdout.write(f'{author}')
