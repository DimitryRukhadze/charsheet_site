from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Race, Theme


# Create your views here.
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
    races_json = serializers.serialize('json', races)
    return Response(races_json)
