from django.test import TestCase
from restaurant.models import Booking, MenuItem

class MenuItemTest(TestCase):
    def test_instance(self):
        item = MenuItem.objects.create(title="Sorbet", price=200, inventory=20)
        self.assertIsInstance(item, MenuItem)
    
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")