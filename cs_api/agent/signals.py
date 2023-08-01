import os
from datetime import datetime

import jwt
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AccessToken, Agent


@receiver(post_save, sender=Agent)
def create_access_token(sender, instance, created, **kwargs):
    if created:
        data = {"agentId": instance.id, "createdAt": str(datetime.now())}
        encoded_jwt = jwt.encode(data, os.environ.get("SECRET"), algorithm="HS256")
        access_token = AccessToken.objects.create(token=encoded_jwt, owner=instance)
        access_token.save()
