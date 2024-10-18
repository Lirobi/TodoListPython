from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    id = forms.IntegerField(label="")
    id.widget = id.hidden_widget()
    name = forms.CharField(max_length=150, label="Name", label_suffix="")
    name.widget.attrs = {"size": "50"}
    completed = forms.BooleanField(required=False, label="Completed", label_suffix="")
    completed.widget.attrs = {"onChange": "save.click()"}
    
    
    class Meta:
        model = TodoItem
        fields = ["id", "name", "completed"]

