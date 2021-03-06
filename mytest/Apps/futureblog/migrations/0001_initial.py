# Generated by Django 3.0.6 on 2020-05-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='futureblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('blog_text', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('futureblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futureblog.futureblog')),
            ],
        ),
    ]
