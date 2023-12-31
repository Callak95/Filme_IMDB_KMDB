from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id", "updated_at", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
        exclude = [
            "last_login",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        ]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs