from django.urls import path

from .views import get_race_by_id


urlpatterns = [
    path('race/<int:id>', get_race_by_id)
]