from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('dashboard',views.dashboard, name='user_dashboard')
]
