# Generated by Django 3.1.2 on 2020-11-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
