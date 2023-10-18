from django.urls import path
from .views import index, subjects, SubjectCreateView, subject, TaskCreateView

urlpatterns = [
    path('new_task <int:subject_id>', TaskCreateView.as_view(), name='create_new_task'),
    path('subject <int:subject_id>', subject, name='subject'),
    path('new_subject/', SubjectCreateView.as_view(), name='create_new_subject'),
    path('subjects/', subjects, name='subjects'),
    path('', index,  name='index_school_log'), 
]
