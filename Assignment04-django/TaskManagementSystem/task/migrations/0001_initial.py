# Generated by Django 4.2.10 on 2024-02-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.TextField(max_length=250)),
                ('isComplete', models.BooleanField(default=False)),
                ('taskAssignDate', models.DateField()),
                ('taskCategory', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]