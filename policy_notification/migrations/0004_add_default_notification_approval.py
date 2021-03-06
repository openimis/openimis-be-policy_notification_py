# Generated by Django 3.0.3 on 2021-06-20 19:31
import logging

from django.db import migrations
from insuree.models import Family

from policy_notification.models import FamilyNotification
from policy_notification.utils import get_default_notification_data

logger = logging.getLogger(__name__)

defaults = get_default_notification_data()

default_approval = defaults['approvalOfNotification']
default_language = defaults['languageOfNotification']

MIGRATION_SQL = f"""
insert into 
tblFamilySMS(FamilyID, ValidityFrom, ApprovalOfSMS, LanguageOfSMS)    
select FamilyId, GETDATE(), 0, '{default_language}' from tblFamilies 
where ValidityTo is null and FamilyID not in (select FamilyID from tblFamilySMS)
"""


class Migration(migrations.Migration):

    dependencies = [
        ('policy_notification', '0003_auto_20210620_1931')
    ]

    operations = [
        migrations.RunSQL(MIGRATION_SQL)
    ]

