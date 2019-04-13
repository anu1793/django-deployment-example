# -*- coding: utf-8 -*-

from django.urls import path
from with_template import views

urlpatterns = [
    path("relative/", views.relative, name ="relative"),
    path("others/", views.others, name ="others"),        
] 