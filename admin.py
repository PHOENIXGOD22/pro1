from django.contrib import admin
from.models import phonebook

# Register your models here.
class phonebookAdmin(admin.ModelAdmin):
    list_display=('Name','Phone')
admin.site.register(phonebook,phonebookAdmin)


