from django.contrib import admin
from .models import NavigationRecord
from .models import Vehicle


class NavigationRecordAdmin(admin.ModelAdmin):
  list_display = ["id","vehicle", "latitude","longitude","date"]
  list_display_links = ["id","vehicle", "latitude","longitude","date"]
  search_fields = ['vehicle']
  list_filter = ['vehicle']
