# Generated by Django 2.0 on 2020-07-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopkeeper',
            old_name='openhours',
            new_name='closetime',
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='opentime',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
