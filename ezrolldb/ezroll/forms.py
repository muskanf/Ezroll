from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'duid', 'major', 'minor', 'PoCRN', 'PrCRN', 'elec']
