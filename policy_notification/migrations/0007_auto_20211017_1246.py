# Generated by Django 3.0.14 on 2021-10-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_notification', '0006_indicationofpolicynotifications_indication_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='indication_details',
            field=models.JSONField(blank=True, db_column='indication_details', default=dict, null=True),
        ),
    ]
