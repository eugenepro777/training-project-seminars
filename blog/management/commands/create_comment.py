from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from blog.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Create comment"

    def handle(self, *args, **kwargs):
        author = Author.objects.order_by('?').first()
        article = Article.objects.order_by('?').first()
        body = lorem_ipsum.paragraph()
        create_date = datetime.now().strftime('%Y-%m-%d')
        update_date = datetime.now().strftime('%Y-%m-%d')
        comment = Comment(
            author=author,
            article=article,
            body=body,
            create_date=create_date,
            update_date=update_date
        )
        comment.save()
        self.stdout.write(f'{comment}')
