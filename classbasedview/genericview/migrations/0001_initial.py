# Generated by Django 4.1.6 on 2023-03-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empoyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.CharField(max_length=5, verbose_name='Emp No.')),
                ('ename', models.CharField(max_length=50, verbose_name='Emp name')),
                ('esal', models.CharField(max_length=10, verbose_name='Emp sal')),
            ],
        ),
    ]
