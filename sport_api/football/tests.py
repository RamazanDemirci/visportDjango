from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import League

from .serializers import LeagueSerializer
from . import views 

from django.test import TestCase
import pymongo

class LeagueTests(APITestCase):
    def setUp(self):
        self.data = {
            "name": "PTT1Lig",
            "alias": "PTT 1 Lig",
            "country": "Turkey",
            "country_code": "TR"
        }
        url = reverse('league_list')
        self.response = self.client.post(url, self.data, format='json')

    def test_api_create_league(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(League.objects.count(), 1)
        self.assertEqual(League.objects.get().name, self.data['name'])

    def test_api_list_leagues(self):
        url = reverse('league_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(League.objects.count(), 1)

    def test_api_can_get_a_league(self):
        league = League.objects.get()
        response = self.client.get(
            reverse('league_detail',
            kwargs={'pk': league.name}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, league)

    def test_api_can_update_a_league(self):
        league = League.objects.get()
        new_data = {
            "country": "Türkiye",
            "country_code": "TRY"
        }
        response = self.client.put(
            reverse('league_detail',
            kwargs={'pk': league.name}), data=new_data, format="json"
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(League.objects.get().name, 'PTT1Lig')

    def test_api_can_delete_a_league(self):
        league = League.objects.get()
        response = self.client.delete(
            reverse('league_detail',
            kwargs={'pk': league.name}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(League.objects.count(), 0)