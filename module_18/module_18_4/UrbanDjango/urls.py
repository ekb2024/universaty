"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    requirements.txt. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    requirements.txt. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    requirements.txt. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  task4.views import *


urlpatterns = [
    path('platform/',func_platform),
    path('platform/games/',func_games),
    path('platform/cart/',func_cart),
    #path('admin/', admin.site.urls),
    #path('', func_template),
    #path('class/', class_template.as_view()),
    #path('', func_template),
]
