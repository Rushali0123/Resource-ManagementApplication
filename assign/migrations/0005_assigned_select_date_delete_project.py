# Generated by Django 4.2.1 on 2023-06-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0004_project_project_end_project_project_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigned',
            name='select_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='project',
        ),
    ]
