# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20161223_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronologyHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('dating_notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='document',
            name='dating_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentpart',
            name='address',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='documentpart',
            name='dating_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='storagelocation',
            name='address',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='chronologyhistory',
            name='document',
            field=models.ForeignKey(related_name='chronology', to='archive.Document'),
        ),
    ]
