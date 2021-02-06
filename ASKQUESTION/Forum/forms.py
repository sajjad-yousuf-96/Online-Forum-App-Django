from django import forms
from .models import forum,Discussion
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateInForum(forms.ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
 
class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
