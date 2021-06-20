from django.urls import path
from .views import (
    ReviewListView,
    ReviewDetailView
)

urlpatterns = [
    path('<int:user_pk>/reviews/', ReviewListView.as_view()),
    path('<int:pk>/reviews/', ReviewDetailView.as_view()),
    path("<int:review_pk>/", ReviewDetailView.as_view()),

]
