from django.urls import path

from .views import races_list


urlpatterns = [
    path('races_list/', races_list)
]