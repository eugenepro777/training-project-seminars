from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:author_id>', views.all_articles, name='all_articles'),
    path('article/<int:article_id>', views.article_page, name='article_page'),
    path('blog/add_author/', views.add_author, name='add_author'),
    path('blog/add_article/', views.add_article, name='add_article'),
]