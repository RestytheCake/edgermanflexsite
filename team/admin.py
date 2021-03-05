from django.contrib import admin

from .models import FileUpload, NickUser, forum_test
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


admin.site.register(FileUpload)
admin.site.register(forum_test)


class NickAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'supporter', 'discord_member', 'admin')
    list_filter = ('admin', 'discord_member', 'discord_name', 'supporter', 'special', 'admin')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('last_login',)}),
        ('Permissions', {'fields': ('active', 'discord_member', 'discord_name',  'supporter', 'special', 'confirm', 'staff', 'admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'discord_name',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(NickUser, NickAdmin)
