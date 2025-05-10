from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, "cms/article_list.html", {"articles": articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "cms/article_detail.html", {"article": article})


def create_article(request):
    if request.method == "POST":
        # Logic to create a new article
        pass
    return render(request, "cms/create_article.html")


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        # Logic to edit the article
        pass
    return render(request, "cms/edit_article.html", {"article": article})


def dashboard(request):
    return HttpResponse("CMS Dashboard")
