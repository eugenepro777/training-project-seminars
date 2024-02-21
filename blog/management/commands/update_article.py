from django.core.management.base import BaseCommand

from blog.models import Article


class Command(BaseCommand):
    help = "Update article by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('title', type=str, help='Article title')
        parser.add_argument('body', type=str, help='Article body')
        parser.add_argument('author_id', type=int, help='ID of the new author')
        parser.add_argument('date', type=str, help='Article new date (YYYY-MM-DD)')
        parser.add_argument('category', type=str, help='Article category')
        parser.add_argument('pub_flag', type=bool, help='Article published (True/False)')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        body = kwargs.get('body')
        author_id = kwargs.get('author_id')
        date = kwargs.get('date')
        category = kwargs.get('category')
        pub_flag = kwargs.get('pub_flag')
        article = Article.objects.filter(pk=pk).first()
        article.title = title
        article.body = body
        article.author_id = author_id
        article.date = date
        article.category = category
        article.pub_flag = pub_flag
        article.save()
        self.stdout.write(f'{article}')
