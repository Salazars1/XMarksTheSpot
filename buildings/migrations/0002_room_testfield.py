# Generated by Django 2.0.3 on 2018-04-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='testField',
            field=models.BooleanField(default=False),
        ),
    ]
