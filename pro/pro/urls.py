"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path("",include('blog.urls')),
    path("reg",include('blog.urls')),
    path("login",include('blog.urls')),
    path("page",include('blog.urls')),
    path("addposts",include('blog.urls')),
    path("addpost",include('blog.urls')),
    path("logout",include('blog.urls')),
    path("delete",include('blog.urls')),
    path('admin/', admin.site.urls),
]
