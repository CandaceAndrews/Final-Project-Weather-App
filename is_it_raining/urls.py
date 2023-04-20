from django.urls import path
from is_it_raining import views

urlpatterns = [
    path("", views.api_root),
    path("weather-animal/<int:original_code>/",
         views.RandomAnimalView.as_view(), name="weather_animal"),
    path("list-animals/", views.AnimalListView.as_view(), name="animal-list"),
    path("captured/<str:name>/", views.CapturedAnimalView.as_view(), name="captured"),
    path("my-animals/", views.UserAnimalList.as_view(), name="my-animals"),
    path("animal-detail/<str:name__iexact>/",
         views.AnimalDetailView.as_view(), name="animal-detail"),
]
