from django.shortcuts import render

from character.models import Race, Theme


def index(request):
    races = list(Race.objects.all())
    themes = list(Theme.objects.all())
    context = {
        'races': races,
        'themes': themes
    }
    return render(request, 'index.html', context=context)