from django.shortcuts import render

from .models import Race


# Create your views here.
def index(request):
    races = list(Race.objects.all())
    return render(request, 'index.html', context={'races': races})
