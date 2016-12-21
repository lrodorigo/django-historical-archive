from django.contrib import admin

# Register your models here.
from archive.models import Document, Photo, Tag, DocumentType, StorageLocation, DocumentCatergory

admin.site.register(Document)
admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(DocumentType)
admin.site.register(StorageLocation)
admin.site.register(DocumentCatergory)