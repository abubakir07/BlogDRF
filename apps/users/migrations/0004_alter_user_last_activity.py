# Generated by Django 4.1.5 on 2023-01-23 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 23, 20, 39, 20, 16544, tzinfo=datetime.timezone.utc), verbose_name='last_activity'),
        ),
    ]
