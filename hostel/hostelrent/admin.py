from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']

admin.site.register(Cleaner)
admin.site.register(Order)
admin.site.register(Room)
admin.site.register(TypeOfNumber)
