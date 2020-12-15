from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.main),
    path('addtodo',views.additem),
    path('deletetodo/<int:item_id>',views.deleteitem),
]
