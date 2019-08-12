from django.test import TestCase
from . import models
from rest_framework.test import APIClient
from rest_framework import status

class TestTestCase(TestCase):
    def setUp(self):
        test_venue = models.Venue.objects.create(name="Foo Bar", description="Test bar description", tagline="Hello world!", image="not real")
        test_user = models.NyteUser.objects.create(email="testing@email.com", password="TestPassword123")
        test_menu_item = models.MenuItem.objects.create(venue=test_venue, name="test beer")
        test_option = models.MenuOption.objects.create(name="test option")
        test_value = models.OptionValue.objects.create(name="test value", option=test_option)
        test_pairing = models.OptionPairing.objects.create(menu_item=test_menu_item, option=test_option)
        test_transaction = models.Transaction.objects.create(user=test_user, venue=test_venue, total=100, data ='{"1":"1"}')

    def test_routes_for_errors(self):
        client = APIClient()

        response = client.get('/api/NyteUser/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/NyteUser/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Venue/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Venue/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/MenuItem/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/MenuItemsByVenue/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Options/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Options/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Transaction/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Transaction/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Venue/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get('/api/Venue/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        