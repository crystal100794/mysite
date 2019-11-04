from django.contrib import admin
from .models import Hero

#we can tell it about Hero.
admin.site.register(Hero)