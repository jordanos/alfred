from agent.models import Agent
from django.db import models


class Session(models.Model):
    agent = models.ForeignKey(
        to=Agent, on_delete=models.CASCADE, related_name="sessions"
    )
    ip = models.CharField(max_length=32, blank=False, null=False)
    host = models.CharField(max_length=250, blank=False, null=False)
    user_agent = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=True)
    session = models.ForeignKey(
        to=Session, on_delete=models.CASCADE, related_name="chats"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
