# Generated by Django 3.0.8 on 2020-11-16 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201103_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
