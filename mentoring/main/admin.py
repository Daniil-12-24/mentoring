from django.contrib import admin
from .models import users

class usersAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'press_count')

admin.site.register(users, usersAdmin)