from rest_framework import serializers

from django.contrib.auth.models import User
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """Snippet/JSON... -> Python OrderedDict"""
    
    # not be used for updating model instances when they are deserialized. 
    # We could have also used CharField(read_only=True) here.
    owner = serializers.ReadOnlyField(source='owner.username')
    # url field to link -> highlight
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url','id', 'highlight', 'owner','title', 'code','linenos', 'language', 'style',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        # snippets is reverse relationship attribute to auth.User
        # by default when using the ModelSerializer class(not include reverse relationship), so we needed to add an explicit field for it.
        fields = ('id', 'username', 'snippets')
