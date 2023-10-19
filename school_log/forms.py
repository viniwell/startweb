from django.forms import ModelForm

from .models import Subject, Task_model

class SubjectModelForm(ModelForm):
    class Meta:
        model= Subject
        fields=('name', )


class TaskModelForm(ModelForm):
    class Meta:
        model= Task_model
        fields=('theme', 'task', 'term', 'subject')



