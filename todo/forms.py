from django import forms
from django.utils.translation import gettext_lazy as _


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Enter todo e.g. Delete junk files'), 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}), localize=True)  