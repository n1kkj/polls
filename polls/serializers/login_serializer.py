from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_null=False, allow_blank=False, write_only=True)
    password = serializers.CharField(allow_null=False, allow_blank=False, write_only=True)
    token = serializers.CharField(max_length=40, read_only=True)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("User is not found")

        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = authenticate(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        return {"token": token.key}
