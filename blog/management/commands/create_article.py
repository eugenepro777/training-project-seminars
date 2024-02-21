from datetime import datetime
from random import choice, randint
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Create a new article"

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        article = Article(
            title=lorem_ipsum.words(10, common=False).capitalize(),
            body=lorem_ipsum.paragraphs(3, common=False),
            date=datetime.now().strftime('%Y-%m-%d'),
            author=choice(authors),
            category=choice(lorem_ipsum.WORDS).capitalize(),
            views_count=randint(1, 99),
            pub_flag=choice([True, False])
        )
        article.save()
        self.stdout.write(f'{article}')

