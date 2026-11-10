"""
URL configuration for auditoria_ecotech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include  # <--- 1. Agregamos 'include' aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sustentabilidad.urls')),  # <--- 2. Agregamos esta línea para conectar tu app
]