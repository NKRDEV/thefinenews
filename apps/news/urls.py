from django.urls import path
from . import views
from .api_views import ArticleListView

urlpatterns = [
    # Example URL patterns
    path("", views.news_list, name="news_list"),
    path("<int:pk>/", views.news_detail, name="news_detail"),
    path("api/articles/", ArticleListView.as_view(), name="article_list_api"),
]
