import requests
from agent.models import AccessToken
from rest_framework import serializers

from .models import Chat, Session


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class SessionSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "agent",
            "ip",
            "host",
            "user_agent",
        ]

    def create(self, validated_data):
        access_token = AccessToken.objects.get(token=validated_data["token"])
        data = {}
        data["user_agent"] = self.context["request"].META.get("HTTP_USER_AGENT")
        data["ip"] = get_client_ip(self.context["request"])
        data["host"] = self.context["request"].META.get("HTTP_HOST")
        validated_data.pop("token")
        session = Session.objects.create(
            **validated_data, **data, agent=access_token.owner
        )
        return session


class ChatSerializer(serializers.ModelSerializer):
    session_id = serializers.IntegerField(required=True, write_only=True)
    question = serializers.CharField(required=True)
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "answer", "session"]

    def create(self, validated_data):
        session = Session.objects.get(id=validated_data["session_id"])
        validated_data.pop("session_id")
        chat = Chat.objects.create(**validated_data, session=session)
        chats = Chat.objects.filter(session=session)
        context = ""
        for ch in chats:
            context += f"question: {ch.question}\n"
            context += f"answer: {ch.answer}\n"
        params = {"question": chat.question, "messages_context": context}
        res = requests.get(url="http://chat-bot:5000/chat", params=params)
        data = res.json()
        chat.answer = data.get("answer")
        chat.save()
        return chat
