from django import forms
from django.contrib.auth import models
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    id = forms.IntegerField(label="")
    id.widget = id.hidden_widget()
    name = forms.CharField(max_length=150, label="Name", label_suffix="")
    name.widget.attrs = {"size": "50", "class": "scale-animation scale-animation-1-02"}
    completed = forms.BooleanField(required=False, label="Completed", label_suffix="")
    completed.widget.attrs = {"onChange": "save.click()", "class": "scale-animation scale-animation-1-1"}
    
    
    class Meta:
        model = TodoItem
        fields = ["id", "name", "completed"]


