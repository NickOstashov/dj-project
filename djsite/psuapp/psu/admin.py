from django.contrib import admin
from psu.models import Problem,FAQ
# Register your models here.

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id','naming','description','icon']
    list_editable = ['description','icon']

@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['id','problem_id','problem','question','answer']
    list_editable = ['question','answer']
    list_filter = ['problem_id']
    