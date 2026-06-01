from django import forms
from accounts.models import User
class Editprofileform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","phone","address","profile_image"]