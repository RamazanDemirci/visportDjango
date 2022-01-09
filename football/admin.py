from django.contrib import admin
from .models import Match, League, Season, Standing

# Register your models here.

admin.site.register(Match)
admin.site.register(League)
admin.site.register(Season)
admin.site.register(Standing)
