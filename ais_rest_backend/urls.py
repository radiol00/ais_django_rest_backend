"""ais_rest_backend URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ais_auth.views import UserViewSet
from absence.views import UserAbsences

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('ais_auth.urls')),
    path('absence/', include('absence.urls')),
    path('user/absence/', UserAbsences.as_view()),
    path('user/', include(router.urls))
]
