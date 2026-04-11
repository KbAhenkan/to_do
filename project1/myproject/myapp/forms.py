from django import forms
from .models import ListModel

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



