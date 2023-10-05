from django.db import models

# Create your models here.

class BoardMessage(models.Model):
    title=models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Опис')
    price=models.FloatField(null=True, blank=True, verbose_name='Ціна')
    published=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')
    rubric=models.ForeignKey("Rubric", null=True, verbose_name='Рубрика', on_delete=models.PROTECT)

    class Meta:
        verbose_name='Оголошення'
        verbose_name_plural='Оголошення'
        ordering=['-published']


class Rubric(models.Model):
    name=models.CharField(max_length=20, db_index=True, verbose_name='Назва')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Рубрика'
        verbose_name='Рубрики'
        ordering=['name']