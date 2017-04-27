from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class NewUserForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    email = forms.CharField(label='E-Mail', widget=forms.EmailInput())
    first_name = forms.CharField(label='First Name', widget=forms.TextInput())
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    recheck_pass = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput())