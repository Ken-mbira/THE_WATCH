# Generated by Django 3.2.8 on 2021-10-31 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required', max_length=50, verbose_name='business name')),
                ('image', models.ImageField(upload_to='images/')),
                ('owner', models.ForeignKey(help_text='owner of business', on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighbourhood.profile', verbose_name='owner of business')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighbourhood.services', verbose_name='services offered')),
            ],
        ),
    ]
