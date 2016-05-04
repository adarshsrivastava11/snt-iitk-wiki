from django import forms

class Login(forms.Form):
	username = forms.CharField(label='User Name',max_length=200)
	team_name = forms.CharField(label='Team Name',max_length=200)