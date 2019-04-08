from rest_framework import serializers
from .models import User, Medication

class UserSerializer(serializers.HyperlinkedModelSerializer):
    medications = serializers.HyperlinkedRelatedField(
        view_name='medication_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'medications')
    
class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    class Meta:
        model = Medication
        fields = ('id', 'name', 'directions', 'servings', 'refill_left', 'user')
