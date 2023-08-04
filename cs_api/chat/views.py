from rest_framework import generics, status
from rest_framework.response import Response

from .models import Chat, Session
from .serializers import ChatSerializer, SessionSerializer


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all().order_by("-id")
    serializer_class = SessionSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatListCreate(generics.ListCreateAPIView):
    queryset = Chat.objects.all().order_by("-id")
    serializer_class = ChatSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
