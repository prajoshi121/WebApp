from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="webhome"),
    path("create-lead", views.create_lead, name="create_lead"),
    path("list-lead", views.list_lead, name="list_lead"),
]
