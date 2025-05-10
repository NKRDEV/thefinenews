from django.contrib import admin
from .models import Article, Category, NewsOwner


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status")  # Removed 'publication_date'
    search_fields = ("title", "content")
    list_filter = ("status", "created_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(NewsOwner)
class NewsOwnerAdmin(admin.ModelAdmin):
    list_display = ("user", "website_url")
    search_fields = ("user__username", "website_url")
