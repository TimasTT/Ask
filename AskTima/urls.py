"""AskTima URL Configuration

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
#from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('ask/', views.ask, name = 'ask'),
    path('login/', views.login, name = 'login'),
    path('settings/', views.settings, name = 'settings'),
    path('signup/', views.signup, name = 'signup'),
    path('', views.index, name = 'main'),
    path('hot', views.hot, name = 'hot'),
    path('question/<int:pk>/', views.question, name = 'question'),
    path('listing/<int:pk>/', views.listing_q, name = 'tag'),
]

