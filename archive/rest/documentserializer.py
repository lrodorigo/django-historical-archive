from rest_framework import serializers

from archive.models import Document


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'description', 'linenos', 'language', 'style')
