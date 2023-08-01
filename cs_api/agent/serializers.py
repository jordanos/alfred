from authentication.serializers import UserSerializer
from rest_framework import serializers

from .models import AccessToken, Agent, SuperPower


class CustomSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            obj, created = self.get_queryset().get_or_create(**{self.slug_field: data})
            return obj
        except (TypeError, ValueError):
            self.fail("invalid")


class SuperPowerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, min_length=3)

    class Meta:
        model = SuperPower
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        return SuperPower.objects.create(**validated_data)


class AccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        return AccessToken.objects.create(**validated_data)


class AgentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250, min_length=3, allow_blank=False)
    super_powers = CustomSlugRelatedField(
        queryset=SuperPower.objects.all(), many=True, slug_field="name"
    )
    owner = UserSerializer(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()),
        read_only=True,
    )

    class Meta:
        model = Agent
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "owner"]

    def create(self, validated_data):
        user = self.context["request"].user
        super_powers_data = validated_data.pop("super_powers", [])
        agent = Agent.objects.create(**validated_data, owner=user)
        for super_power in super_powers_data:
            t, _ = SuperPower.objects.get_or_create(name=super_power.name)
            agent.super_powers.add(t)
        return agent

    def update(self, instance, validated_data):
        super_powers_data = validated_data.pop("super_powers", [])
        instance = super().update(instance, validated_data)
        super_powers = [
            SuperPower.objects.get_or_create(name=super_power.name)[0]
            for super_power in super_powers_data
        ]
        instance.super_powers.set(super_powers)
        return instance
