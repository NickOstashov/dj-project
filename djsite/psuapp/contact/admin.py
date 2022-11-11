from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname','email','tel']
    list_editable = ['name','surname','email','tel']
    