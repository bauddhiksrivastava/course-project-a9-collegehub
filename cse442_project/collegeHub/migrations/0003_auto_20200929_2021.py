# Generated by Django 2.2.12 on 2020-09-29 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeHub', '0002_auto_20200929_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='collegeHub.User'),
        ),
    ]
