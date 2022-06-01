from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddressSerialzer


# Create your views here.
class AddressViewSet(ModelViewSet):
    serializer_class= AddressSerialzer
    queryset=Address.objects.all()