from django.contrib import admin

from .models import FileUpload, NickUser, forum, profile, comment, notification
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


admin.site.register(FileUpload)
admin.site.register(forum)
admin.site.register(comment)
admin.site.register(profile)
admin.site.register(notification)


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
        ('Dates', {'fields': ('last_login',)}),
        ('Role\'s', {'fields': ('discord_member', 'discord_name', 'supporter', 'special')}),
        ('Permissions', {'fields': ('active', 'confirm', 'staff', 'admin',)}),
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
