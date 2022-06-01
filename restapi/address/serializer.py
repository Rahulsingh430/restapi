from dataclasses import field
from rest_framework.serializers import ModelSerializer;
from .models import Address;



class AddressSerialzer(ModelSerializer):
  class Meta:
      model= Address
      fields= '__all__'
