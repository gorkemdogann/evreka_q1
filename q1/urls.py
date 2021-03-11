from django.contrib import admin
from django.urls import path, include
from evraka import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.Index, name='index'),
  path('evraka/', include('evraka.urls')),

]
