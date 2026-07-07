from django import forms
from backend.models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['order','reference_design','content_details']
        