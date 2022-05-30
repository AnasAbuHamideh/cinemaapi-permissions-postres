from rest_framework import serializers
from films.models import Film


class FilmsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Film
        fields = ('title','date_published','updated' ,'actors','watcher', 'description', 'published')