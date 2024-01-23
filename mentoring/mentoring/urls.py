from django.contrib import admin
from django.urls import path, include

from main.views import index, count

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('count/', count, name='count'),
    path('admin/', admin.site.urls),
]
