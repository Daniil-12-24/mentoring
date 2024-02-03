from django.contrib import admin
from django.urls import path

from main.views import index, count, login, signin, my_account, edit_profile

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('count/', count, name='count'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('my_account/<int:user_id>/<str:user_login>/', my_account, name='my_account'),
    path('edit_profile/<int:user_id>/<str:user_login>/', edit_profile, name='edit_profile'),
    path('admin/', admin.site.urls),
]
