# Generated by Django 5.1.4 on 2025-01-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qms_app', '0005_remove_uploadedevidencefile_milestone_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedevidencefile',
            name='file_url',
        ),
        migrations.AddField(
            model_name='uploadedevidencefile',
            name='file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
