from django import forms

from members.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('author', 'age')