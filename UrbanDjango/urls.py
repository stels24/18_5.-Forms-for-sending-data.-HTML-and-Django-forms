"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from task5.views import *
from django.views.generic import TemplateView


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', all_main),
#     path('class/', all_class.as_view()),
#     path('func/', all_func),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', registration_page),
#     path('shop/', shop_page),
#     path('bin/', bin_page),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
    path('html_sign_up/', sign_up_by_html, name='html_sign_up'),
]