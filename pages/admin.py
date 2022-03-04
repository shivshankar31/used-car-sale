from django.contrib import admin
from pages.models import Teams

# Register your models here.


class TeamsAdmin(admin.ModelAdmin):
    # list_fields = '__all__'
    fieldsets = (
        (None, {
            'fields': ('firstname', 'lastname', 'designation', 'photo',)
        }),
        ('Add Social Media Links', {
            # 'classes': ('collapse',),
            'fields': ('facebook_link', 'twitter_link','insta_link'),
        }),
    )
    
    list_display = ('firstname', 'lastname', 'designation', 'created_date')

admin.site.register(Teams,TeamsAdmin)