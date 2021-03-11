from django.contrib import admin
from django.urls import path
from . import views

app_name = "evraka"

urlpatterns = [
  path('dashboard/',views.Dashboard, name='dashboard'),
  path('addexpedition/',views.addEvraka, name='addevraka'),
  path('update/<int:id>',views.UpdateEvraka, name='update'),
  path('delete/<int:id>',views.DeleteEvraka, name='delete'),
]
