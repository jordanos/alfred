from django.contrib import admin

from .models import AccessToken, Agent, SuperPower


# Register your models here.
class AccessTokenAdmin(admin.ModelAdmin):
    pass


class AgentAdmin(admin.ModelAdmin):
    pass


class SuperPowerAdmin(admin.ModelAdmin):
    pass


admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(SuperPower, SuperPowerAdmin)
