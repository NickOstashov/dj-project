from django.contrib import admin
# from psu.models import Problem,FAQ
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from users.forms import CustomUserCreationForm, CustomUserChangeForm
# from users.models import CustomUser

# # Register your models here.

# @admin.register(Problem)
# class ProblemAdmin(admin.ModelAdmin):
#     list_display = ['id','naming','description','icon']
#     list_editable = ['description','icon']

# @admin.register(FAQ)
# class FaqAdmin(admin.ModelAdmin):
#     list_display = ['id','problem_id','problem','question','answer']
#     list_editable = ['question','answer']
#     list_filter = ['problem_id']

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# admin.site.register(CustomUser, CustomUserAdmin)
