# Generated by Django 5.1.7 on 2025-03-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
