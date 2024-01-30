from django.contrib import admin
from django.urls import path

from main.views import index, count, login, signin, greetings

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('count/', count, name='count'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('greetings/<str:user_name>/<int:user_count>/', greetings, name='greetings'),
    path('admin/', admin.site.urls),
]
