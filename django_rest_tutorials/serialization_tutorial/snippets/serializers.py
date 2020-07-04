from rest_framework import serializers

from django.contrib.auth.models import User
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """Snippet/JSON... -> Python OrderedDict"""
    
    # not be used for updating model instances when they are deserialized. 
    # We could have also used CharField(read_only=True) here.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'owner','title', 'code', 'linenos', 'language', 'style',)


class UserSerializer(serializers.ModelSerializer):
    snippets =  serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        # snippets is reverse relationship attribute to auth.User
        # by default when using the ModelSerializer class(not include reverse relationship), so we needed to add an explicit field for it.
        fields = ['id', 'username', 'snippets']
