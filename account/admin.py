from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Contact, Friend

admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(Friend)