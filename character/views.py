from django.shortcuts import render

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
