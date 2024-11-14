# forms.py
from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'attachments']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }