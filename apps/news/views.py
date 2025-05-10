from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm


def news_list(request):
    return HttpResponse("News List")


def news_detail(request, pk):
    return HttpResponse(f"News Detail for ID {pk}")


def news_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("news_list"))
    else:
        form = ArticleForm()
    return render(request, "news/news_form.html", {"form": form})


def news_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("news_detail", args=[pk]))
    else:
        form = ArticleForm(instance=article)
    return render(request, "news/news_form.html", {"form": form})


def news_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return HttpResponseRedirect(reverse("news_list"))
    return render(request, "news/news_confirm_delete.html", {"article": article})
