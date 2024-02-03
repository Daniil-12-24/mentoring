from django.contrib import admin
from .models import users, user_data

class usersAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'press_count')

class userDataAdmin(admin.ModelAdmin):
    list_display = ('login', 'u_password', 'u_email', 'press_count')

admin.site.register(users, usersAdmin)
admin.site.register(user_data, userDataAdmin)