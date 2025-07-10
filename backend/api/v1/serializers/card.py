from rest_framework import serializers

from card.models import Card
from api.v1.serializers.user import UserSerializer



class CardSerializer(serializers.ModelSerializer):

    doctor = UserSerializer(source='doctor_id.profile', read_only=True)
    date_of_birth = serializers.DateField(format="%d.%m.%Y", required=False)
    date_card = serializers.DateField(format="%d.%m.%Y", required=False)

    class Meta:
        model = Card
        
        fields = "__all__"
    