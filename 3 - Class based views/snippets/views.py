from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# View Baseada em classes
class SnippetList(APIView):
    # se o método for get
    def get(self, request):
        # pega todos os itens dentro da tabela
        snippets = Snippet.objects.all()
        # serializa transformando em json
        serializer = SnippetSerializer(snippets, many=True)
        # retorna os itens coletados
        return Response(serializer.data)

    def post(self, request):
        # serializa os itens recebidos para o python ler
        serializer = SnippetSerializer(data=request.data)
        # verifica se o formulario é valido
        if serializer.is_valid():
            # se for valido salva
            serializer.save()
            # Retorna os dados e o status de create
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # se os dados nao forem válidos retorna erro no status
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


# View Baseada em classes
class SnippentDetail(APIView):
    # função que procura o objeto dentro da base de dados
    def get_object(self, pk):
        try:
            # procura o pk do item e o retorna
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # caso não encontre, retorna um erro 404
            raise Http404

    # se o método for get
    def get(self, request, pk):
        # executa a função introduzindo dentro da variavel o valor recebido
        snippet = self.get_object(pk)
        # serializa para json o item encontrado
        serializer = SnippetSerializer(snippet)
        # retorna o item encontrado como json
        return Response(serializer.data)

    # se o método for put
    def put(self, request, pk):
        # executa a função introduzindo dentro da variavel o valor recebido
        snippet = self.get_object(pk)
        # verifica serializa para dentro da base de dados
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            # se for valido salva
            serializer.save()
            # Retorna os dados e o status de create
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # se os dados nao forem válidos retorna erro no status
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # verifica se o objeto existe
        snippet = self.get_object(pk)
        # deleta o objeto
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------

# View Baseada em classes com mixins
# importe os mixins que irá utilizar
class SnippetMixinsList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # para realizar alterações
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# View Baseada em classes com mixins
# importe os mixins que irá utilizar
class SnippentMixinsDetail(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    # passar para classe a base de dados que deseja
    queryset = Snippet.objects.all()
    # o serializador
    serializer_class = SnippetSerializer

    # caso deseje alterar alguma coisa
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# -----------------------------------------------------

# View Baseada em classes com generics
# importe os generics que irá utilizar
class SnippetGenericsList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# View Baseada em classes com generics
# importe os generics que irá utilizar
class SnippentGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
