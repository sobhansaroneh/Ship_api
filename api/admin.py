from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User ,Event , Booked

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Booked)