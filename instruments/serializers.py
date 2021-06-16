from django.db import models
from rest_framework import  fields, serializers
from .models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):    
    class Meta: 
        model = Instrument
        fields = '__all__'

