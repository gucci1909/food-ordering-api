# Generated by Django 5.1.5 on 2025-02-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_new_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='new_field_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
