from django import forms

class UserUpdate(forms.Form):
    username = forms.CharField(label='Username', max_length=191, required=False)
    first_name = forms.CharField(label='First Name', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)
    email = forms.EmailField(label='Email', max_length=191, required=False, help_text='Please enter a valid Xavier email address.')