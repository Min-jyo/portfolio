from django.contrib import admin

# Register your models here.
from many_to_one.models import Manufacturer, Car, WPSUser


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(WPSUser)
class WPSUserAdmin(admin.ModelAdmin):
    pass

