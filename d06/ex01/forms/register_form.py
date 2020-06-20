from django import forms
from ..models import TipUser

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = TipUser

    def register(self):
        clean_data=self.cleaned_data
        if not TipUser.objects.filter(username=clean_data['username']).exists() and clean_data['password1'] == clean_data['password2']:
            new_user = TipUser(username=clean_data['username'], password=clean_data['password1'])
            new_user.save()
            return True
        else:
            return False
    