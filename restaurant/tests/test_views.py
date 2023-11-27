from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Booking, MenuItem
from restaurant.serializers import MenuItemSerializer
from restaurant.views import MenuItemsView
from django.test import TestCase, Client


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", password="test_user_password")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        MenuItem.objects.create(title="Caipirinha", price=14, inventory=40)
        MenuItem.objects.create(title="Risotto", price=20, inventory=50)
        MenuItem.objects.create(title="Lasagne", price=12, inventory=70)
        MenuItem.objects.create(title="Pizza", price=15, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu-list/'))
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        print(response.data)
        print(serializer.data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)