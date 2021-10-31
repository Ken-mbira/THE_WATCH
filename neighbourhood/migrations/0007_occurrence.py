# Generated by Django 3.2.8 on 2021-10-31 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0006_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required', max_length=50, verbose_name='ocurrence name')),
                ('description', models.TextField(help_text='format: required', verbose_name='occurence description')),
                ('image_description', models.ImageField(upload_to='images/')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('to_happen_at', models.DateTimeField(blank=True, null=True, verbose_name='scheduled time')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_events', to='neighbourhood.neighbourhood')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reported_events', to='neighbourhood.profile')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='occurred_events', to='neighbourhood.eventtype')),
            ],
        ),
    ]
