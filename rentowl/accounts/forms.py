from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
class Registerform(UserCreationForm):
    phone=forms.CharField(required=False)
    address=forms.CharField(widget=forms.Textarea())
    profile_image=forms.ImageField(required=False)
    class Meta:
        model=User
        fields=['username','email','password1','password2','phone','address','profile_image']
        help_texts = {'username': '', 'email': '', 'password1': '', 'password2': ''}

    def __init__(self, *args, **kwargs):  #to remove help text in forms
        super().__init__(*args, **kwargs)
        # Remove help_text dynamically
        for field_name, field in self.fields.items():
            field.help_text = None



#------ login form ----
class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # give unique IDs
        self.fields['username'].widget.attrs.update({'id': 'login_username'})
        self.fields['password'].widget.attrs.update({'id': 'login_password'})