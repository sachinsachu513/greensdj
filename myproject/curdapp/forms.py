from django import forms
from.models import employees1


class employeeform(forms.ModelForm):
    class Meta:
        model=employees1
        fields="__all__"