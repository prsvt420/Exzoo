from django.contrib.auth import get_user_model


from products import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[User] = get_user_model()
        exclude: tuple = (
            'is_active',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'groups',
            'password',
        )
        ref_name: str = 'CustomDjoserUser Serializer'
        read_only_fields: tuple = ('is_active', 'is_staff', 'is_superuser')
