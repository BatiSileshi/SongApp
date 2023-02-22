from rest_framework import serializers
from song.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        