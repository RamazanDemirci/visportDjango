
from unicodedata import name
from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from rest_framework.test import APIClient

from ..models import League


@before.each_feature
def before_each_feature(feature):
    world.client = APIClient()



@step('I empty the "([^"]+)" table')
def step_empty_table(self, model_name):
    get_model(model_name).objects.all().delete()

  

@step('I create the following leagues:')
def step_create_leagues(self):
    League.objects.bulk_create([
        League(
            name=
            
        ) for data in guess_types(self.hashes)
    ])