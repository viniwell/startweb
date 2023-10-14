from django.shortcuts import render
from .models import Subject

# Create your views here.
def index(request):
    context={}
    return render(request, 'school_log/index.html', context)

def subjects(request):
    subjects=sorted(Subject.objects.all())
    context={
        'subjects':subjects
    }
    return render(request, 'school_log/subjects.html', context)