from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer, SnippetSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este conjunto de visualizações fornece automaticamente ações `list` e` detail`.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    Este conjunto de visualizações fornece automaticamente `list`,` create`, `retrieve`,
     ações `update` e` destroy`.

     Além disso, também fornecemos uma ação extra `destaque`.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Se o usuario colocar na request /snippets/2/highlight/
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # se a request for pra salvar liga o campo do usuario com o user da request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def api_root(request):
    return Response(
        {
            'users': reverse('user-list', request=request),
            'snippets': reverse('snippet-list', request=request)
        })
