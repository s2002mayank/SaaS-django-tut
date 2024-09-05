# Generated by Django 5.0.8 on 2024-08-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_subscriptionprice_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionprice',
            name='features',
        ),
        migrations.AddField(
            model_name='subscription',
            name='features',
            field=models.TextField(blank=True, help_text='features for pricing, seperated by new line', null=True),
        ),
    ]