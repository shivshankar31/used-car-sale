from django.contrib import admin
from cars.models import Car

# Register your models here.



class CarsAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            "fields": ('car_title', 'model', 'color', 'year', 'price', 'city', 'state'),
        }),
        ('Body ', {
            'fields': ('body_style','doors', 'features', 'interior', 'passenger' )
        }),
        ('Engine Type ', {
            'fields': ('engine', 'trasmission', 'vin_no', 'miles', 'millage', 'fuel_type' )
        }),
        ( 'condition', {
            'fields': ( 'description', 'no_of_owners', 'is_featured' )
        }),
        ( 'Photo', {
            # 'classes': ('collapse',), # to ide the below fields
            'fields': ('car_photo','car_photo1', 'car_photo2', 'car_photo3', 'car_photo4', 'car_photo5' )
        }),
    
    )
    



admin.site.register(Car,CarsAdmin)





