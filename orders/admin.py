from django.contrib import admin

from .models import toppings, menu, order





class Toppings(admin.ModelAdmin):
    fields=("topping")




admin.site.register(toppings)
admin.site.register(menu)
admin.site.register(order)
