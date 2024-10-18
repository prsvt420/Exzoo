from django.contrib.auth import get_user_model

from products import serializers


class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:

        model = get_user_model()
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
