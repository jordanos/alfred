from authentication.permissions import IsAdmin
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import AccessToken, Agent, SuperPower
from .serializers import AccessTokenSerializer, AgentSerializer, SuperPowerSerializer


class AccessTokenList(generics.ListAPIView):
    queryset = AccessToken.objects.all().order_by("-id")
    serializer_class = AccessTokenSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all().order_by("-id")
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ["ADMIN"]:
            return Agent.objects.all().order_by("-id")
        return Agent.objects.filter(owner=user).order_by("-id")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuperPowerList(generics.ListCreateAPIView):
    queryset = SuperPower.objects.all().order_by("-id")
    serializer_class = SuperPowerSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
