from django.urls import path
from .views import index, subjects, SubjectCreateView, subject

urlpatterns = [
    path('subject <int:subject_id>', subject, name='subject'),
    path('new_subject/', SubjectCreateView.as_view(), name='create_new_subject'),
    path('subjects/', subjects, name='subjects'),
    path('', index,  name='index_school_log'), 
]
