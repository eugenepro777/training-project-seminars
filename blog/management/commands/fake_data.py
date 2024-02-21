from datetime import datetime
from random import choice, randint

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from django.utils.crypto import get_random_string

from blog.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Generate fake authors, articles and comments."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of Author')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        year = [str(i) for i in range(1900, 2014)]
        month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        date_range = [str(i).zfill(2) for i in range(1, 28)]
        # date = f'{choice(year)}-{choice(month)}-{choice(date)}'
        for _ in range(1, count + 1):
            first_name = get_random_string(length=7,
                                           allowed_chars='abcdefghijklmnopqrstuvwxyz').capitalize()
            last_name = get_random_string(length=7,
                                          allowed_chars='abcdefghijklmnopqrstuvwxyz').capitalize()
            author = Author(
                first_name=first_name,
                last_name=last_name,
                email=f'{first_name.lower()}@gmail.com',
                bio=lorem_ipsum.paragraph(),
                birth_date=f'{choice(year)}-{choice(month)}-{choice(date_range)}'
            )
            author.save()
            article = Article(
                title=lorem_ipsum.words(10, common=False).capitalize(),
                body=lorem_ipsum.paragraphs(2, common=False),
                date=f'{choice(year)}-{choice(month)}-{choice(date_range)}',
                author=author,
                views_count=randint(1, 99),
                category=choice(lorem_ipsum.WORDS).capitalize(),
                pub_flag=choice([True, False])
            )
            article.save()
            for _ in range(1, count * 2):
                comment = Comment(
                    author=author,
                    article=article,
                    body=lorem_ipsum.paragraph(),
                    create_date=f'{choice(year)}-{choice(month)}-{choice(date_range)}',
                    update_date=datetime.now().strftime('%Y-%m-%d')
                )
                comment.save()
