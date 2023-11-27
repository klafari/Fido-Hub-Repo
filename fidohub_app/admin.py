# Resources
from .models import Client, DogWalker, Dog

from django.contrib import admin

# Models that can be registered
admin.site.register(Client)
admin.site.register(DogWalker)
admin.site.register(Dog)
