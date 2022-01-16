import pytest
from .models import League
from django.urls import reverse


@pytest.mark.django_db
def test_league_create():
  League.objects.create_user('PTT1Lig','PTT 1 Lig','Turkey','TR')
  assert League.objects.count() == 1

@pytest.mark.django_db
def test_view(client):
   url = reverse('league_list')
   response = client.get(url)
   assert response.status_code == 200


def test_always_passes():
    print('Fixture for module')
    return 1


def test_always_fails():
    print('Fixture for module')
    return 1