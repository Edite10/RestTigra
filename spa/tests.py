from django.test import TestCase
from django.urls import reverse

class SpaHomeViewTests(TestCase):
    def test_spa_home_view(self):
        response = self.client.get(reverse('spa:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Rest Tigra Spa!")
