from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("cms/", include("apps.cms.urls")),
    path("news/", include("apps.news.urls")),
]
