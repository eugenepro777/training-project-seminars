from django.contrib import admin
from blog.models import Article, Author, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category']
    readonly_fields = ['date', 'views_count']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Текст статьи',
                'fields': ['title', 'body'],
            },
        ),
        (
            'Категория и дата публикации и изменения',
            {
                'fields': ['category', 'date'],
            }
        ),
        (
            'Число просмотров и статус',
            {
                'description': 'Статистика просмотров',
                'fields': ['views_count', 'pub_flag'],
            }
        ),

    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'email']
    readonly_fields = ['birth_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['full_name'],
            },
        ),
        (
            'Биография автора',
            {
                'classes': ['collapse'],
                'description': 'Биография',
                'fields': ['bio', 'birth_date'],
            },
        ),
        (
            'Контакты',
            {
                'description': 'Контактная информация',
                'fields': ['email'],
            }
        ),

    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'create_date', 'update_date']
    readonly_fields = ['create_date', 'update_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author', 'article'],
            },
        ),
        (
            'Список комментариев',
            {
                'classes': ['collapse'],
                'description': 'Комментарий',
                'fields': ['body'],
            },
        ),
        (
            'Хронология',
            {
                'description': 'Дата создания и изменения',
                'fields': ['create_date', 'update_date'],
            }
        ),

    ]