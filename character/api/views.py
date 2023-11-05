from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from character.models import Race, Theme


class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


@api_view(['POST'])
def get_race_by_id(request):
    race_id = request.data
    race = Race.objects.get(id=race_id)
    races_serializer = RaceSerializer(data=[race], many=True)
    races_serializer.is_valid()
    response_data = races_serializer.data[0]
    print(response_data)
    return Response(response_data)