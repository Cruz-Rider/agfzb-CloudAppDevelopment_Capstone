from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 4

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_origin', 'estd_year', 'website', 'logo', 'description', 'contact', )
    search_fields = ('name', 'country_of_origin')
    inlines = [CarModelInline]
    
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'year', 'type', 'price', 'features', 'dealer_id')
    list_filter = ('car_make', 'year', 'type')
    search_fields = ('name', 'car_make__name')
