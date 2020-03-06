from django.contrib import admin

from .models import Pizza, Topping

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass

