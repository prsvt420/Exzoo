from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class UserTests(APITestCase):
    def setUp(self) -> None:
        """Setup for tests"""
        user_model: User = get_user_model()

        self.user: user_model = user_model.objects.create_user(
            username='user',
            email='exzoo_user@gmail.com',
            password=r'fdjknasdf7843dfFGYudfdsy'
        )

        self.token: Token = Token.objects.create(user=self.user)

    def test_user_me(self) -> None:
        """Test for user me endpoint"""
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )
        user_me_url: str = reverse(viewname='user-me')
        response: Response = self.client.get(path=user_me_url)

        self.assertEqual(first=response.status_code, second=status.HTTP_200_OK)
