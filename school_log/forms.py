from django.forms import ModelForm

from .models import Subject

class SubjectModelForm(ModelForm):
    class Meta:
        model= Subject
        fields=('name', )
