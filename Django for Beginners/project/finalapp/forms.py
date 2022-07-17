from django import forms
from .models import *


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()


class TaskForm(forms.ModelForm):  # since we already have the model
    class Meta:
        model = Task
        # fields = '__all__'  # Hey inherit all the attributes
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})  # so the date time can work well
        }
