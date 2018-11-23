from django import forms
from .models import *


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = SubscriptionsModels
        fields = ('name', 'email', 'telefone', 'message')