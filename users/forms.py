from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerDetails

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['name', 'email', 'address', 'city', 'state', 'zip_code', 'phone']  # Exclude 'user' field
        widgets = {
            # You can use widgets to style or hide fields if needed
        }
