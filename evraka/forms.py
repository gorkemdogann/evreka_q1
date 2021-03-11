from django import forms
from .models import NavigationRecord

class NavigationRecordForm(forms.ModelForm):
  class Meta:
    model=NavigationRecord
    fields = ["id","user","vehicle", "latitude","longitude","plate"]
