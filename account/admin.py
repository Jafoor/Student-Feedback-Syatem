from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(Teacher)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name',  'last_name',)
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    # list_display = ('email', 'username', 'first_name',  'last_name',
    #                 'is_active', 'is_staff')
    # fieldsets = (
    #     (None, {'fields': ('email', 'username', 'first_name', 'last_name',)}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    #
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
    #      ),
    # )

admin.site.unregister(User)
admin.site.register(User, UserAdminConfig)
admin.site.register(Dept)
admin.site.register(Batch)
admin.site.register(Semester)
admin.site.register(Staff)
