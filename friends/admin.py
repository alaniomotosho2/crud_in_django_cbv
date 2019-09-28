from django.contrib import admin

# Register your models here.
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']


# or 
# admin.site.register(Person)