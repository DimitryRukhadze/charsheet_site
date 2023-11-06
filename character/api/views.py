from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from character.models import Race, Theme


class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


@api_view(['GET'])
def get_race_by_id(request, race_id):
    race = Race.objects.get(id=race_id)
    races_serializer = RaceSerializer(race)
    response_data = races_serializer.data
    return Response(response_data)