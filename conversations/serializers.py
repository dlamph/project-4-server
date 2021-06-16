from django.db import models
from rest_framework import  fields, serializers
from jwt_auth.serializers import NestedUserSerializer
from .models import Conversation
# from django.contrib.auth import get_user_model


class ConversationSerializer(serializers.ModelSerializer):   
    
    class Meta: 
        model = Conversation
        fields = '__all__'

class PopulatedConversationSerializer(ConversationSerializer):

    sender = NestedUserSerializer()
    receiver = NestedUserSerializer()

