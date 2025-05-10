from django.db import models
from django.contrib import admin
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cms_articles"
    )  # Add a unique related_name
    categories = models.ManyToManyField("Category", related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title


class NewsOwner(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cms_newsowner"
    )  # Add a unique related_name
    website_url = models.URLField()

    def __str__(self):
        return self.user.username


@admin.register(Article)  # This registers the Article model with ArticleAdmin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    search_fields = ("title", "content")
    list_filter = ("published_date", "status")
