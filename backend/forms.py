from django import forms
from .models import OrderModel

class AdminOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'