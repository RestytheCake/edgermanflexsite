from django.contrib import admin
from .models import FileUpload, NickUser, forum_test

# Register your models here.


admin.site.register(FileUpload)
admin.site.register(NickUser)
admin.site.register(forum_test)
