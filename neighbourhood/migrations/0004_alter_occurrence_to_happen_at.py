# Generated by Django 3.2.8 on 2021-11-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_alter_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='to_happen_at',
            field=models.DateField(blank=True, null=True, verbose_name='scheduled time'),
        ),
    ]