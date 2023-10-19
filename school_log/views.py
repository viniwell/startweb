from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Subject, Task_model
from .forms import SubjectModelForm, TaskModelForm

# Create your views here.
class SubjectCreateView(CreateView):
    template_name='school_log/create_new_subject.html'
    form_class=SubjectModelForm
    success_url=reverse_lazy('index_school_log')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        return context
    

class TaskCreateView(CreateView):
    template_name='school_log/create_new_task.html'
    form_class=TaskModelForm
    success_url=reverse_lazy('subjects')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['task']=Task_model.objects.all()

        return context


def index(request):
    context={}
    return render(request, 'school_log/index.html', context)

def subjects(request):
    subjects=Subject.objects.all()
    context={
        'subjects':subjects
    }
    return render(request, 'school_log/subjects.html', context)

def subject(request, subject_id):
    subject=Subject.objects.get(id=subject_id)
    tasks=Task_model.objects.filter(subject=subject_id)
    context={
        'tasks':tasks,
        'subject':subject,
    }
    return render(request, 'school_log/subject.html', context)

def task(request, task_id):
    task=Task_model.objects.get(id=task_id)
    context={
        'task':task,
    }
    return render(request, 'school_log/task.html', context)




