from django import forms
from .models import ListModel
from django.contrib.auth.models import User

class List(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = '__all__'

        labels = {
            'Title' : "Title:",
            'Description' : "Description:",
            'Due_date' : "Due Date:",
    }
        widgets = {
            'Title':forms.TextInput(
                attrs={'placeholder':'e.g Wash Dishes', 'class': 'form-control'}),
            'Description': forms.Textarea(
                attrs={'rows': 4}),
            'Due_date': forms.DateInput(attrs={'type':'date'}),
        }

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
    
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data