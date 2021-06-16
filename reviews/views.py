from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework import status

from reviews.models import Review
from .serializers import ReviewSerializer, PopulatedReviewSerializer

# Create your views here.
class ReviewListView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        reviews = Review.objects.all()
        serialized_reviews = PopulatedReviewSerializer(reviews, many=True)
        return Response(serialized_reviews.data, status.HTTP_200_OK)

    def post(self, request, user_pk):
        request.data[''] = user_pk
        request.data['owner'] = request.user.id
        serialized_review = ReviewSerializer(data=request.data)
        if serialized_review.is_valid():
            serialized_review.save()
            return Response(serialized_review.data, status=status.HTTP_201_CREATED)
        return Response(serialized_review.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ReviewDetailView(APIView):

    def delete(self, request, _user_pk, review_pk):
        try:
            review_to_delete = Review.objects.get(pk=review_pk)
            if review_to_delete.owner != request.user:
                raise PermissionDenied()
            review_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            raise NotFound()
