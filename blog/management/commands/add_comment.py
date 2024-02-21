from django.core.management.base import BaseCommand
from blog.models import Article, Author, Comment


class Command(BaseCommand):
    help = 'Добавление комментария к статье'

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int, help='Article ID')
        parser.add_argument('author_id', type=int, help='Author ID')
        parser.add_argument('comment_body', type=str, help='Comment text')

    def handle(self, *args, **kwargs):
        article_id = kwargs['article_id']
        author_id = kwargs['author_id']
        comment_body = kwargs['comment_body']

        try:
            article = Article.objects.get(pk=article_id)
            author = Author.objects.get(pk=author_id)

            comment = Comment.objects.create(
                article=article,
                author=author,
                body=comment_body,
            )
            self.stdout.write(self.style.SUCCESS(f'Комментарий <{comment}> успешно добавлен'))

        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR('Статья с таким ID не существует'))
        except Author.DoesNotExist:
            self.stdout.write(self.style.ERROR('Автор с таким ID не существует'))
