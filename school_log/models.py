from django.db import models
from django import forms

# Create your models here.

class Task_model(models.Model):
    theme=models.CharField(max_length=75, verbose_name='Тема')
    task=models.TextField(null=True, blank=True, verbose_name='Завдвння')
    term=models.DateTimeField(null=True, db_index=True, verbose_name='Термін здачі')
    published=models.DateTimeField(auto_now_add=True, verbose_name='Опубліковано')
    subject=models.ForeignKey("Subject", null=True, verbose_name='Рубрика', on_delete=models.PROTECT)

    class Meta:
        verbose_name='Завдання'
        verbose_name_plural='Завдання'
        ordering=['-published']
    
class Subject(models.Model):
    name=models.CharField(max_length=20, verbose_name='Предмет')

    class Meta:
        verbose_name='Предмет'
        verbose_name_plural='Предмети'
