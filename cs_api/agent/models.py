from django.contrib.auth import get_user_model
from django.db import models


class SuperPower(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    super_powers = models.ManyToManyField(SuperPower)
    owner = models.ForeignKey(
        to=get_user_model(),
        related_name="agents",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AccessToken(models.Model):
    token = models.CharField(max_length=250, blank=False, null=False, unique=True)
    owner = models.OneToOneField(
        to=Agent, on_delete=models.DO_NOTHING, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
