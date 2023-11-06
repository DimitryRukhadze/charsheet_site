from django.urls import path

from .views import get_race_by_id


urlpatterns = [
    path('race/<int:race_id>', get_race_by_id)
]