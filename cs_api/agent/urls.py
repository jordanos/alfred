from django.urls import path

from .views import AccessTokenList, AgentList, SuperPowerList

urlpatterns = [
    path("", AgentList.as_view(), name="agents"),
    path("super-powers/", SuperPowerList.as_view(), name="super-powers"),
    path("tokens/", AccessTokenList.as_view(), name="tokens"),
]
