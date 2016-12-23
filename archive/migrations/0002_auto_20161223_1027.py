# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documentcatergory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentpart',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentpart',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documentpart',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='storagelocation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='videoannotation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
