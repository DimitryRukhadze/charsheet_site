from django.urls import path

from .views import get_race_by_id


urlpatterns = [
    path('races_list/', get_race_by_id)
]