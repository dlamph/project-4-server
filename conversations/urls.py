from conversations.models import Conversation
from django.urls import path
from .views import ( ConversationsListView, ConversationsDetailView )


urlpatterns = [
    path('',ConversationsListView.as_view()),
    path('<int:pk>/conversations/', ConversationsDetailView.as_view()),
]
