from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo


def check_name_length(value):
    if len(value) < 2:
        raise forms.ValidationError("NAME TOO SHORT!")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_name_length])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
        validators=[validators.MaxValueValidator(0)]
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("EMAILS DO NOT MATCH")

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = '__all__'

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
