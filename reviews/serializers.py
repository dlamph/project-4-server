from rest_framework import serializers
from jwt_auth.nested import NestedUserSerializer

from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'

class PopulatedReviewSerializer(ReviewSerializer):
    user = NestedUserSerializer(many=True)
    owner = NestedUserSerializer(many=True)

