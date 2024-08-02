# Generated by Django 5.0.6 on 2024-06-14 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0004_remove_conferencebyyear_conf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceComplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.conferencebyyear')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conferencename')),
            ],
        ),
        migrations.AddField(
            model_name='conferencebyyear',
            name='conf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.conferencename'),
        ),
        migrations.DeleteModel(
            name='Conference',
        ),
    ]