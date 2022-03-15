from django.contrib import admin
from pages.models import Teams
from django.utils.html import format_html

# Register your models here.


class TeamsAdmin(admin.ModelAdmin):
    # list_fields = '__all__'

    # to diaplay thumbnail photo 
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style = "border-radius: 5px;" />'.format(object.photo.url))

    # to change the coloum name 
    thumbnail.short_discription = 'Image'

    # to display fields in show more option 
    fieldsets = (
        (None, {
            'fields': ('firstname', 'lastname', 'designation', 'photo',)
        }),
        ('Add Social Media Links', {
            # 'classes': ('collapse',),
            'fields': ('facebook_link', 'twitter_link','insta_link'),
        }),
    )
    
    # to display the fields in admin panel
    list_display = ('id','thumbnail','firstname', 'lastname', 'designation', 'created_date')
    list_display_links =('id','thumbnail','firstname') # helps to make editable by clicking on id and firstname

    search_fields = ('firstname', 'designation')
    list_filter = ('designation',)
admin.site.register(Teams,TeamsAdmin)