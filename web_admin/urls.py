"""Food_Delivery_DupliCate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web_admin import views

urlpatterns = [
    path('', views.showIndex, name='pwn_main'),
    path('pwn_login_check/', views.pwn_login_check, name='pwn_login_check'),
    path('welcome/', views.welcome, name='welcome'),
    path('state/', views.openState, name='state'),
    path('city/', views.openCity, name='city'),
    path('cuisine/', views.openCusine, name='cuisine'),
    path('vendor/', views.openVendor, name='vendor'),
    path('resports/', views.openReporsts, name='reports'),
    path('logout/', views.pwn_login_check, name='logout'),

    path('state_save/', views.state_save, name='state_save'),
    path('update_state/',views.update,name='update_state'),
    path('delete_state/',views.delete_state,name='delete_state'),

    path('city_save/',views.city_save,name='city_save'),
    path('update_city/',views.update_city,name='update_city'),
    path('delete_city/',views.delete_city,name='delete_city'),

    path('cuisine_save/',views.cuisine_save,name='cuisine_save'),
    path('update_cui/',views.update_cui,name='update_cui'),
    path('delete_cui/',views.delete_cui,name='delete_cui')


]
