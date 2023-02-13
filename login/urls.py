from django.contrib import admin
from django.urls import path
from django.urls import include
from login.views import login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/<str:username>',login),
    path('login')
]
