from django.contrib import admin

# Register your models here.
from .models import Plane,Passenger

admin.site.register(Plane)
admin.site.register(Passenger)