from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "status")
    search_fields = ("title", "content")
    list_filter = ("status", "published_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
