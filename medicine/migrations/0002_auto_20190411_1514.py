# Generated by Django 2.2 on 2019-04-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
