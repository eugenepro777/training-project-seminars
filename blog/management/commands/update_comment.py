from django.core.management.base import BaseCommand

from blog.models import Comment


class Command(BaseCommand):
    help = "Update comment by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('body', type=str, help='Comment body')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = kwargs.get('body')
        comment = Comment.objects.filter(pk=pk).first()
        comment.body = body
        comment.save()
        self.stdout.write(f'{comment}')
