# Generated by Django 5.0.1 on 2024-01-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Collage', '0010_alter_studentresultsheet_matched_sheet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresultsheet',
            old_name='matched_sheet',
            new_name='matched_sheet_b64',
        ),
    ]
