from django.contrib import admin

# Register your models here.
from .models import Package, Contact, Booking

admin.site.register(Package)
admin.site.register(Contact)
admin.site.register(Booking)