from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def save(self,commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.email = self.clean_password2['email']
        if commit:
            user.save()
        return user