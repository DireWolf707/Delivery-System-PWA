from django import forms
from django.contrib.auth import get_user_model
from .models import Customer


class BasicUserInfoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'age')


class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('avatar',)
