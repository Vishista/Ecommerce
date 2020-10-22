from django import forms
from .models import Order




class SaveInDB(forms.ModelForm):
    class Meta:
      model= Order
      fields = [
        'user',
        'products',
        'total',
        'address',
        'timestamp',
        'phone',
      ]