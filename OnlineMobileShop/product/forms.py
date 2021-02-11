from django.forms import ModelForm
from django import forms
from product.models import Brand,Mobile,Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            'brand_name':forms.TextInput(attrs={'class':'form-control'})
        }

class BrandEditForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            'brand_name':forms.TextInput(attrs={'class':'form-control'})
        }

class MobileCreateFrm(ModelForm):
    class Meta:
        model=Mobile
        fields = "__all__"
        widgets={
            'mobile_name':forms.TextInput(attrs={'class':'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'camera': forms.TextInput(attrs={'class': 'form-control'}),
            'os': forms.TextInput(attrs={'class': 'form-control'}),

        }

class MobileEditFrm(ModelForm):
    class Meta:
        model=Mobile
        fields = "__all__"
        widgets={
            'mobile_name':forms.TextInput(attrs={'class':'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'camera': forms.TextInput(attrs={'class': 'form-control'}),
            'os': forms.TextInput(attrs={'class': 'form-control'}),

        }

class OrderFrm(ModelForm):
    class Meta:
        model=Orders
        fields="__all__"
        widgets={
            "productid":forms.TextInput(attrs={'readonly':'readonly'}),
            "status":forms.HiddenInput(),
            "user":forms.HiddenInput(),
        }

class OrderUpdateFrm(ModelForm):
    class Meta:
        model=Orders
        fields="__all__"

class SearchForm(forms.Form):
    Brand_name=forms.CharField(max_length=120)

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]