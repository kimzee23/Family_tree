from django import forms
from django.contrib.auth.models import User
from .models import TreeShare

class TreeShareForm(forms.ModelForm):
    shared_with: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=User.objects,
        label="Shared With"
    )

    class Meta:
        model = TreeShare
        fields = ['tree', 'shared_with', 'access_type']
