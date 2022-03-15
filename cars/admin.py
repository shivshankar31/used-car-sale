from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

# Register your models here.



class CarsAdmin(admin.ModelAdmin):

    # to diaplay thumbnail photo 
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style = "border-radius: 40px;" />'.format(object.car_photo.url))

    # to change the coloum name 
    thumbnail.short_discription = 'Car Image'

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
            'fields': ( 'description','no_of_owners', 'is_featured' )
        }),
        ( 'Photo', {
            # 'classes': ('collapse',), # to ide the below fields
            'fields': ('car_photo','car_photo1', 'car_photo2', 'car_photo3', 'car_photo4', 'car_photo5' )
        }),
           
    )
    
    list_display = ('id','thumbnail','car_title', 'color','year','fuel_type', 'price','city','created_date', 'is_featured')
    list_editable = ('is_featured',)
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('car_title', 'color','year','fuel_type')
    list_filter =('city', 'fuel_type','body_style')



admin.site.register(Car, CarsAdmin)





