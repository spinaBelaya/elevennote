from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer): # converts compex data as queryset or model instances to readable objects as JSON or smth like that 

    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'pub_date')
