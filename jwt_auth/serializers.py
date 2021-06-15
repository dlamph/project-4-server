from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from reviews.serializers import ReviewSerializer
# from reviews.models import Review
# from django.db.models import fields
from .models import User

from .nested import NestedUserSerializer


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})

        try:
            validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

        data['password'] = make_password(password)

        return data

    class Meta:
        model = User
        fields = '__all__'

#Can we use a nested user to return the information that we want to display
# on our user profile page? With the details in fields.
    # class NestedUserSerializer(serializers.ModelSerializer):

    #     class Meta:
    #         model = User
    #         fields = ('id', 'username', 'profile_image', )


class PopulatedUserSerializer(NestedUserSerializer):
    reviews_received = ReviewSerializer(many=True)
    reviews_posted = ReviewSerializer(many=True)
