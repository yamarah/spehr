from django import forms
from django.contrib.auth.models import User
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        lables = {
            'password1': 'Password',
            'password2':'Confirm Password'
        }

class UserProForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student,'student'),
        (parent,'parent'),
    ]
    user_type = forms.ChoiceField(required=True,choices=user_types)
    class Meta:
        model = UserPro
        fields = ('bio','profile_pic','user_type')
