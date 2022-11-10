from django.contrib import admin
from psu.models import Problem
# Register your models here.

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id','naming','description','icon']
    list_editable = ['description','icon']
    pass