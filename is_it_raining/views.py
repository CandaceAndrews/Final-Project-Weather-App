import random
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters, status
from rest_framework.views import APIView

from .models import User, Weather, Animal, CapturedAnimal
from .serializers import WeatherSerializer, AnimalSerializer, CapturedAnimalSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response()


class AnimalListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetailView(generics.RetrieveAPIView):
    '''fetch random animal of weather type given in url
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_object(self, *args, **kwargs):
        original_code = self.kwargs["original_code"]
        weather_code = (str(original_code))[0]
        animals = Animal.objects.filter(weather__weather_code=weather_code)
        animals = list(animals)
        random_animal = random.choice(animals)
        return random_animal


class CapturedAnimalView(APIView):

    def post(self, request, name):
        owner = request.user

        animal = get_object_or_404(Animal, name=name)

        captured = CapturedAnimal.objects.create(owner=owner, animal=animal)

        serializer = CapturedAnimalSerializer(captured)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
