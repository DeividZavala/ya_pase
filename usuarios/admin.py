from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Permission

admin.site.register(UserProfile)
admin.site.register(Permission)


