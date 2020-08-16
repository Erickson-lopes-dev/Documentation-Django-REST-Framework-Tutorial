from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


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


# Retornando hyper link para quando a view for solicitado o método GET
@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'users': reverse('user-list', request=request),
            'snippets': reverse('snippet-list', request=request)
        })


# retornando os objetios especificados de um item na tabela
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    # renderiza como html / se tirar retorna só os dados
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
