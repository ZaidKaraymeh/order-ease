from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['style'] = 'height:50px;'
        self.fields['password'].widget.attrs['style'] = 'height:50px;'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm):
    
    class Meta:
        # Interacts with User model
        model = CustomUser
        # What fields to show and in which order
        fields = ["first_name", "last_name", "email",
                  "password1", "password2", "phone_number"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['first_name'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['last_name'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['email'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['password1'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['password2'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['phone_number'].widget.attrs['style'] = 'width:100%; height:50px;'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'

"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
"""
