from conversations.models import Conversation
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ConversationSerializer, PopulatedConversationSerializer



class ConversationsDetailView(APIView):

    permission_classes=(IsAuthenticated, )

    def post(self, request ,pk):
        request.data['sender'] = request.user.id
        request.data['receiver'] =pk
        message_to_create = PopulatedConversationSerializer(data=request.data)
        if message_to_create.is_valid():
            message_to_create.save()
            return Response(message_to_create.data, status=status.HTTP_201_CREATED)
        return Response(message_to_create.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)


class ConversationsListView(APIView):
    permission_classes=(IsAuthenticated, )
    def get(self, _request):
        conversations = Conversation.objects.all()
        serlialized_conversations = PopulatedConversationSerializer(conversations,many=True)
        return Response(serlialized_conversations.data, status=status.HTTP_200_OK)