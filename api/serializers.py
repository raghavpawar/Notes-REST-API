from .models import notes
from rest_framework import serializers
from django.contrib.auth.models import User

# using the model serializer to serialize the notes model
class NotesSerializer(serializers.ModelSerializer):
    # since owner is an external relation, we'll have to specify its serialization separately
    owner = serializers.ReadOnlyField(source='owner.username') 
    class Meta:
        model = notes
        fields = ['id', 'title', 'content', 'image', 'created', 'owner']


