# Generated by Django 2.2.2 on 2019-06-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20190617_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='confluence_page',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='jira_ticket',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
