# Generated by Django 4.2.1 on 2023-06-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0005_assigned_select_date_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigned',
            name='select_date',
        ),
        migrations.AddField(
            model_name='addassigned',
            name='select_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='addbillable',
            name='select_date',
            field=models.DateField(null=True),
        ),
    ]