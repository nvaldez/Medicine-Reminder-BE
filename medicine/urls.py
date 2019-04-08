from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('medications', views.MedicationList.as_view(), name='medications_list'),
    path('medication/<int:pk>', views.MedicationDetail.as_view(), name='medication_detail'),
]