from rest_framework import generics
from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer

class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets or crete a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
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
