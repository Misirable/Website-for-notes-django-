from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Form


class TaskForm(ModelForm):               #Принимает данные от модели task(из models)
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class FilterForm(Form):
    class Meta:
        fields = ['task_filter']
        widgets = {
            'task_filter': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }
