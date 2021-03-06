# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 10:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dating_notes', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('pages', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCatergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='archive.DocumentCatergory')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dating_notes', models.TextField()),
                ('position', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('progressive_number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('codename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('position', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VideoAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('time', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileDocument',
            fields=[
                ('documentpart_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.DocumentPart')),
            ],
            bases=('archive.documentpart',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('documentpart_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.DocumentPart')),
            ],
            bases=('archive.documentpart',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('documentpart_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.DocumentPart')),
            ],
            bases=('archive.documentpart',),
        ),
        migrations.AddField(
            model_name='documentpart',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='archive.Document'),
        ),
        migrations.AddField(
            model_name='documentpart',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='archive.DocumentType'),
        ),
        migrations.AddField(
            model_name='document',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='documents', to='archive.DocumentCatergory'),
        ),
        migrations.AddField(
            model_name='document',
            name='storage_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='archive.StorageLocation'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='documents', to='archive.Tag'),
        ),
        migrations.AddField(
            model_name='videoannotation',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='archive.Video'),
        ),
    ]
