# Generated by Django 3.0.3 on 2021-06-20 19:31
import logging

from django.db import migrations, models
from core.models import ModuleConfiguration

logger = logging.getLogger(__name__)


def __config_already_exists():
    sc = ModuleConfiguration.objects.filter(module='policy_notification', layer='be')
    return sc.count() > 0


def create_admin_panel_configuration(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    if __config_already_exists():
        logger.warning(F"Configuration for module already stored in database")
        return

    configuration = ModuleConfiguration(
        module='policy_notification', layer='be', version='1.0.0',
        is_exposed=False, config="""{
    "providers": {
        "eGASMSGateway": {
            "GateUrl": "http://127.0.0.1:8001",
            "SmsResource": "/api/policy_notification/test_sms/",
            "PrivateKey": "",
            "UserId": "",
            "SenderId": "",
            "ServiceId": "",
            "RequestType": "",
            "HeaderKeys": "X-Auth-Request-Hash,X-Auth-Request-Id,X-Auth-Request-Type",
            "HeaderValues": "PrivateKey,UserId,RequestType"
        },
        "TextNotificationProvider": {
            "DestinationFolder": "sent_notification"
        }
    },
    "eligibleNotificationTypes": {
        "activation_of_policy": false,
        "starting_of_policy": false,
        "need_for_renewal": false,
        "expiration_of_policy": false,
        "reminder_after_expiration": false,
        "renewal_of_policy": false
    }
}""")
    configuration.save()


class Migration(migrations.Migration):

    dependencies = [
        ('policy_notification', '0002_indicationofpolicynotifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='activation_of_policy',
            field=models.DateTimeField(db_column='NotificationOnActivationSent', null=True),
        ),
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='expiration_of_policy',
            field=models.DateTimeField(db_column='NotificationOnExpirationSent', null=True),
        ),
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='need_for_renewal',
            field=models.DateTimeField(db_column='NotificationBeforeExpirySent', null=True),
        ),
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='reminder_after_expiration',
            field=models.DateTimeField(db_column='NotificationAfterExpirationSent', null=True),
        ),
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='renewal_of_policy',
            field=models.DateTimeField(db_column='NotificationOnRenewalSent', null=True),
        ),
        migrations.AlterField(
            model_name='indicationofpolicynotifications',
            name='starting_of_policy',
            field=models.DateTimeField(db_column='NotificationOnEffectiveSent', null=True),
        ),
        migrations.RunPython(create_admin_panel_configuration, reverse_code=migrations.RunPython.noop),
    ]
