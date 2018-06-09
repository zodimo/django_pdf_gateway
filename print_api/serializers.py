from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from print_api.models import Pdfgen

from rest_framework import serializers

class PdfGenSerializer(serializers.ModelSerializer):
    # rendered_file = serializers.ReadOnlyField()
    download_link = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model=Pdfgen
        fields = ('id','name', 'content', 'website','download_link')

    def validate(self, data):
        if not data['content'] and not data['website']:
            raise serializers.ValidationError('Content or Website is required.')

        return data
