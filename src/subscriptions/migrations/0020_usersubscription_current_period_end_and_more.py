# Generated by Django 5.0.8 on 2024-08-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_usersubscription_user_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='current_period_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='current_period_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='original_period_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
