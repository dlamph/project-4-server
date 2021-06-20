from django.contrib.auth import get_user_model
from reviews.serializers import ReviewSerializer
from .nested import NestedUserSerializer

User = get_user_model()

class PopulatedUserSerializer(NestedUserSerializer):
    reviews_received = ReviewSerializer(many=True)
    reviews_posted = ReviewSerializer(many=True)

    class Meta:
        model = User
        fields = (
          'id',
          'username',
          'profile_image',
          'email',
          'instrument_type',
          'location_type_choices',
          'reviews_received',
          'reviews_posted',
          'first_name',
          'bio',
          'last_name',
          'user_type'
        )
