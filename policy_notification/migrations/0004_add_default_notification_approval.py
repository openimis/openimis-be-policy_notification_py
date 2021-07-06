# Generated by Django 3.0.3 on 2021-06-20 19:31
import logging

from django.db import migrations
from insuree.models import Family

from policy_notification.models import FamilySMS
from policy_notification.utils import get_default_notification_data

logger = logging.getLogger(__name__)

defaults = get_default_notification_data()


def __create_family_approval(family):
    new_approval = FamilySMS(
        approval_of_notification=defaults['approvalOfNotification'],
        language_of_notification=defaults['languageOfNotification'],
        family=family
    )
    new_approval.save()


def add_defaults_family_notification_approval(apps, schema_editor):
    for family in Family.objects.filter(validity_to=None).all():
        try:
            family_sms = Family.family_sms
            if family_sms:
                __create_family_approval(family)
        except FamilySMS.DoesNotExist:
            __create_family_approval(family)


class Migration(migrations.Migration):

    dependencies = [
        ('policy_notification', '0003_auto_20210620_1931')
    ]

    operations = [
        migrations.RunPython(add_defaults_family_notification_approval, reverse_code=migrations.RunPython.noop)
    ]
