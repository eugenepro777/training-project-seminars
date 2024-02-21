from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Article
from .forms import AuthorForm, ArticleForm


def index(request):
    return render(request, 'blog/index.html')


def all_articles(request, author_id):
    # author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author_id=author_id)
    return render(request, 'blog/blog.html', {'articles': articles})


def article_page(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.order_by('update_date')
    article.views_count += 1
    article.save()
    return render(request, 'blog/article.html', {'article': article, 'comments': comments})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            bio = form.cleaned_data.get('bio')
            birth_date = form.cleaned_data.get('birth_date')
            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                bio=bio,
                birth_date=birth_date
            )
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'blog/add_author.html', {'form': form})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            date = form.cleaned_data.get('date')
            author = form.cleaned_data.get('author')
            category = form.cleaned_data.get('category')
            views_count = form.cleaned_data.get('views_count')
            pub_flag = form.cleaned_data.get('pub_flag')
        article = Article.objects.create(
            title=title,
            body=body,
            date=date,
            author=author,
            category=category,
            views_count=views_count,
            pub_flag=pub_flag
        )
        return redirect('add_article')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})
