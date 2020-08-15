from django.contrib.auth.models import User
from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetGenericsList(generics.ListCreateAPIView):
    # Associando a criação do owner ao usuario
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SnippentGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    # opções de permissão
    permission_classes = [
        # se o usuario estiver authenticado ele tem todas as permissoes caso contratio apenas leitura
        permissions.IsAuthenticatedOrReadOnly,
        #  Permissões de gravação são permitidas apenas para o proprietário do objeto.
        IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# com generic de listagem/Somente leitura
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# com generic de Detalhe/Somente leitura
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
