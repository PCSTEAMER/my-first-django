from django.contrib import admin

# Register your models here.
from myapp.models import Person
class manageperson(admin.ModelAdmin):
    list_display = ('name', 'age', 'date_of_birth', 'address', 'email')
admin.site.register(Person, manageperson)