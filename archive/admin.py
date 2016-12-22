from django.contrib import admin

# Register your models here.
from archive.models import Document, Photo, Tag, DocumentType, StorageLocation, DocumentCatergory

class DocumentTypeAdminInline(admin.TabularInline):
    model = DocumentCatergory

class StorageLocationAdminInline(admin.TabularInline):
    model = StorageLocation

@admin.register(Document, Photo)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ['categories', 'tags', 'title']
    pass

#admin.site.register(Document)
#admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(DocumentType)
admin.site.register(StorageLocation)
admin.site.register(DocumentCatergory)