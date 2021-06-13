from django.db import models
from rest_framework import  fields, serializers
from .models import Instrument
# Feedback

class InstrumentSerializer(serializers.ModelSerializer):    
    class Meta: 
        model = Instrument
        fields = '__all__'

# class FeedbackSerlializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Feedback
#         fields = '__all__'

# class PopulatedTeacherSerialiser(TeacherSerialiser):
#     feedbacks = FeedbackSerlializer(many=True)
