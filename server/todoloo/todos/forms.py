from django import forms
from todos.models import *
from dataclasses import fields

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'completed'
        ]
