from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


# API root entry point
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets or crete a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    # Associate snippets with Users (@Override)
    # generics.ListCreateAPIView.post() -> self.create(..., owner) 
    # Also Validation with Request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Delete a code-snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    rendered_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object() # Returns the object the view is displaying.
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    """
    To Show List of Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve User Data (get_object_or_404(queryset, pk=pk))
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
