from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from products import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model: User = get_user_model()
        exclude: tuple = (
            'is_active',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'groups',
            'password',
            'last_login'
        )
        read_only_fields: tuple = ('is_active', 'is_staff', 'is_superuser')
