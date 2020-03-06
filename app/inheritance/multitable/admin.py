from django.contrib import admin

from .models import Place1, Restaurant1

@admin.register(Place1)
class Place1Admin(admin.ModelAdmin):
    pass

@admin.register(Restaurant1)
class Restuarant1Admin(admin.ModelAdmin):
    pass
