from django import forms

class RegisterForm(forms.Form):
    nickname = forms.CharField( max_length = 35)
    email = forms.EmailField()
    avatar = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
	nickname = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(max_length=510,widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.CharField(max_length=100)