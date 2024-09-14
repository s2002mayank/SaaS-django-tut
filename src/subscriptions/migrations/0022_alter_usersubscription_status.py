# Generated by Django 5.0.8 on 2024-08-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0021_usersubscription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('trialing', 'Trialing'), ('incomplete', 'Incomplete'), ('incomplete_expired', 'Incomplete Expired'), ('past_due', 'Past Due'), ('canceled', 'Canceled'), ('unpaid', 'Unpaid'), ('paused', 'Paused')], max_length=20, null=True),
        ),
    ]
