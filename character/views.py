from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Race, Theme


class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


def index(request):
    races = list(Race.objects.all())
    themes = list(Theme.objects.all())
    context = {
        'races': races,
        'themes': themes
    }
    return render(request, 'index.html', context=context)


@api_view(['GET'])
def races_list(request):
    races = Race.objects.all()
    races_serializer = RaceSerializer(data=races, many=True)
    races_serializer.is_valid()
    response_data = races_serializer.data
    return Response(response_data)
