# Register your models here.

from django.contrib import admin

from aplicativo.models import Car

class CarFilter(admin.ModelAdmin):
    list_display = ("id", "model", "brand", "year") 
    list_display_links = ("id", "model", "brand", "year") 
    list_filter = ("model", "year") 
    search_fields = ("model", "brand") 

admin.site.register(Car, CarFilter)