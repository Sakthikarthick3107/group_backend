from django.contrib import admin
from .models import CollegeEvents,Register

# Register your models here.

class CollegeEventsAdmin(admin.ModelAdmin):
    list_display = ('event_name' , 'description' , 'seats',)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('participant_name','email','event_id')

admin.site.register(CollegeEvents,CollegeEventsAdmin)
admin.site.register(Register , RegisterAdmin)
