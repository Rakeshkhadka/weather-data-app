# Generated by Django 4.2.1 on 2023-05-13 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0003_rename_weather_data_sourcedata"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="weathersummary",
            options={"ordering": ["-id"]},
        ),
    ]
