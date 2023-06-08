from django.forms import ModelForm
from data.models import task

class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'status', 'priority', 'description']
