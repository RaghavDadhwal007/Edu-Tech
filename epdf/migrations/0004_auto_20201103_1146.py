# Generated by Django 3.1.2 on 2020-11-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epdf', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=225, unique=True),
        ),
    ]
