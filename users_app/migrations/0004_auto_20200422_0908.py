# Generated by Django 3.0.5 on 2020-04-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]