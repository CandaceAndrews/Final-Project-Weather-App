from django.urls import path
from is_it_raining import views

urlpatterns = [
    path("", views.api_root),
]