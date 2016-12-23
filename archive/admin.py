from django.contrib import admin

# Register your models here.
from archive.models import Document, Photo, Tag, DocumentType, StorageLocation, DocumentCatergory, DocumentPart, Video


def make_inline(_model):
    class TempInline(admin.TabularInline):
        model = _model

    return TempInline



@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [make_inline(DocumentPart), make_inline(Photo), make_inline(Video)]

#admin.site.register(Document)
#admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(DocumentType)
admin.site.register(StorageLocation)
admin.site.register(DocumentCatergory)