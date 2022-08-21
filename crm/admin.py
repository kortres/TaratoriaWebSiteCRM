from django.contrib import admin
from .models import Userinfo, Homework, Calendar
# Register your models here.

admin.site.register(Userinfo)
admin.site.register(Homework)
admin.site.register(Calendar)
