from django.db import models
from django.utils import timezone


class NavigationRecord(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, verbose_name='Kullanıcı',null=True)
  vehicle = models.CharField(max_length=60, verbose_name='Araç', null=True)
  # date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi', null=True)
  date = models.DateTimeField(default=timezone.now)
  latitude = models.FloatField(verbose_name='Enlem')
  longitude = models.FloatField(verbose_name='Boylam')
  plate = models.CharField(max_length=10, verbose_name="Araç Plakası", null=True)


class Vehicle(models.Model):
  id = models.AutoField(primary_key=True)
  plate = models.CharField(max_length=10, verbose_name="Araç Plakası")
