# Generated by Django 3.2.8 on 2021-10-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0007_occurrence'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]