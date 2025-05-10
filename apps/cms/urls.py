from django.urls import path
from . import views

urlpatterns = [
    # Example URL patterns
    path("", views.dashboard, name="cms_dashboard"),
]
