"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import login as tan90_login
from . import course_manage as tan90_course_manage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^do_login/', tan90_login.do_login),
    url(r'^do_logout/', tan90_login.do_logout),
    url(r'^do_register/', tan90_login.do_register),
    url(r'^get_category/', tan90_course_manage.get_category),
    url(r'^add_category/', tan90_course_manage.add_category),
    url(r'^del_category/', tan90_course_manage.del_category),
    url(r'^add_course/', tan90_course_manage.add_course),
    url(r'^delete_course/', tan90_course_manage.del_course),
    url(r'^get_all_courses/', tan90_course_manage.get_all_courses),
    url(r'^add_course_cover/', tan90_course_manage.add_course_cover),
]
