# Generated by Django 4.1.7 on 2023-10-05 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='boardmessage',
            options={'ordering': ['-published'], 'verbose_name': 'Оголошення', 'verbose_name_plural': 'Оголошення'},
        ),
        migrations.AlterField(
            model_name='boardmessage',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='boardmessage',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='boardmessage',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано'),
        ),
        migrations.AlterField(
            model_name='boardmessage',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='boardmessage',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='board.rubric', verbose_name='Рубрика'),
        ),
    ]
