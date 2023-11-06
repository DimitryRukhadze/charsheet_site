from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from character.models import Race, Theme


class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


@api_view(['GET'])
def get_race_by_id(request, id):
    race = Race.objects.get(id=id)
    races_serializer = RaceSerializer(data=[race], many=True)
    races_serializer.is_valid()
    response_data = races_serializer.data
    print(response_data)
    return Response(response_data)