from django import forms

class DjangoForm(forms.Form):
    text_field = forms.CharField(max_length=100)
