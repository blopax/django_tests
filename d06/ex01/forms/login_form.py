from django import forms
from ..models import TipUser

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = TipUser

    def login(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        success = False
        try:
            user = TipUser.objects.get(username=username)
            if user.password == password:
                success = True
            
        finally:
            return success

