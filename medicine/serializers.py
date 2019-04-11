from rest_framework import serializers
from .models import  Medication


    
class MedicationSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(
    #     read_only=True
    # )
    class Meta:
        model = Medication
        fields = ('id', 'name', 'directions', 'servings', 'refill_left')

# class UserSerializer(serializers.ModelSerializer):
#     medications = MedicationSerializer(
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'medications')
