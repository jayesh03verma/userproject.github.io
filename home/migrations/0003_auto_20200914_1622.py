# Generated by Django 3.1.1 on 2020-09-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
