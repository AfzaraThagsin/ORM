# Generated by Django 4.2.5 on 2023-10-31 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_football_delete_employee"),
    ]

    operations = [
        migrations.RenameField(
            model_name="football",
            old_name="Yrs_Of_Exp",
            new_name="place",
        ),
    ]
