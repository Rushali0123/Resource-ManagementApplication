# Generated by Django 4.2.1 on 2023-06-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_start',
            field=models.DateField(null=True),
        ),
    ]
