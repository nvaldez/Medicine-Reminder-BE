from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, MedicationSerializer
from .models import User, Medication

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicationList(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class =MedicationSerializer
