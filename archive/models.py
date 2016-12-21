from __future__ import unicode_literals

from django.contrib.gis.db.models.fields import PointField
from django.db import models
from django.db.models import CharField, TextField, DateField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.forms import ImageField


class TitleDescrptionModel(models.Model):
    title = CharField(max_length=255, null=True, blank=True)
    description = TextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        app_label = 'archive'


class DatebleModel(models.Model):
    start_date = DateField()
    end_date = DateField()

    class Meta:
        abstract = True
        app_label = 'archive'


class DocumentCatergory(TitleDescrptionModel):
    parent = ForeignKey('DocumentCatergory', null=True, blank=True)

    class Meta:
        app_label = 'archive'


class Tag(models.Model):
    tag = CharField(max_length=100)

    class Meta:
        app_label = 'archive'

    def __str__(self):
        return


class PositionableModel(models.Model):
    position = PointField(blank=True, null=True)
    address = TextField(default="")
    city = CharField(max_length=200, blank=True, null=True, default="")
    state = CharField(max_length=200, blank=True, null=True, default="")

    class Meta:
        abstract = True
        app_label = 'archive'


class StorageLocation(TitleDescrptionModel, PositionableModel):

    class Meta:
        app_label = 'archive'


class DocumentType(TitleDescrptionModel):
    codename = CharField(max_length=200, )

    class Meta:
        app_label = 'archive'


class Document(TitleDescrptionModel, DatebleModel, PositionableModel):
    type = ForeignKey(DocumentType, null=False, blank=False)

    tags = ManyToManyField('Tag', blank=True, )

    categories = ManyToManyField('DocumentCatergory', blank=True, )

    storage_location = ForeignKey(StorageLocation)

    class Meta:
        app_label = 'archive'


class Photo(Document):
    image = ImageField(required=False, )
    thumbnail = ImageField(required=False, )

    class Meta:
        app_label = 'archive'


class DocumentAggregate(TitleDescrptionModel, ):
    documents = ManyToManyField('Document')

    class Meta:
        app_label = 'archive'
