from django.urls import path
from .views import index, subjects

urlpatterns = [
    path('subjects/', subjects, name='subjects'),
    path('', index,  name='index_school_log'), 
]
