from __future__ import unicode_literals

from django.contrib.gis.db.models.fields import PointField
from django.db import models
from django.db.models import CharField, TextField, DateField, IntegerField
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.forms import ImageField, FileField


class TitleDescrptionModel(models.Model):
    title = CharField(max_length=255, null=True, blank=True)
    description = TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        app_label = 'archive'


class DatebleModel(models.Model):
    start_date = DateField(blank=True, null=True)
    end_date = DateField(blank=True, null=True)

    dating_notes = TextField(blank=True)

    class Meta:
        abstract = True
        app_label = 'archive'


class DocumentCatergory(TitleDescrptionModel):
    parent = ForeignKey('DocumentCatergory', null=True, blank=True, related_name='childs')

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
    address = TextField(default="", blank=True)
    city = CharField(max_length=200, blank=True, null=True, default="")
    state = CharField(max_length=200, blank=True, null=True, default="")

    class Meta:
        abstract = True
        app_label = 'archive'


class StorageLocation(TitleDescrptionModel, PositionableModel):
    class Meta:
        app_label = 'archive'


class ChronologyHistory(TitleDescrptionModel, DatebleModel):
    document = ForeignKey('Document', related_name='chronology')


class DocumentType(TitleDescrptionModel):
    codename = CharField(max_length=200, )

    class Meta:
        app_label = 'archive'


class DocumentPart(TitleDescrptionModel, DatebleModel, PositionableModel):
    parent = ForeignKey('Document', blank=False, null=False, related_name='parts')
    type = ForeignKey(DocumentType, null=False, blank=False, related_name='documents')

    progressive_number = IntegerField(blank=True)

    class Meta:
        app_label = 'archive'


class Photo(DocumentPart):
    image = ImageField(required=False, )
    thumbnail = ImageField(required=False, )

    class Meta:
        app_label = 'archive'


class Video(DocumentPart):
    file = FileField(required=False, )

    class Meta:
        app_label = 'archive'


class VideoAnnotation(TitleDescrptionModel):
    time = IntegerField(blank=False)

    video = ForeignKey('Video', null=False, blank=False, related_name="annotations")


FILE_DOCUMENT_TYPES = (('pdf', 'PDF.DOCUMENT'),
                       ('other', 'OTHER'))


class FileDocument(DocumentPart):
    file = FileField(required=False, )

    class Meta:
        app_label = 'archive'


class Document(TitleDescrptionModel, DatebleModel):
    tags = ManyToManyField('Tag', blank=True, related_name='documents')

    categories = ManyToManyField('DocumentCatergory', blank=True, related_name='documents')

    storage_location = ForeignKey(StorageLocation, related_name='documents')

    is_visible = BooleanField(default=True, blank=False, null=False)

    pages = IntegerField(blank=True)

    class Meta:
        app_label = 'archive'
