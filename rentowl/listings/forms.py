from django import forms
from listings.models import Products


class Productform(forms.ModelForm):
    class Meta:
        model=Products
        fields=['title','category','rent_price','description','deposit_price','image']


