from django.urls import path

from .views import ChatListCreate, SessionListCreate

urlpatterns = [
    path("", ChatListCreate.as_view(), name="chats"),
    path("sessions/", SessionListCreate.as_view(), name="sessions"),
]
