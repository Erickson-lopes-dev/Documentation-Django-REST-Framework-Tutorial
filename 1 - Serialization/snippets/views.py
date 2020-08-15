from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    """
        lista todos ou adiciona
    """
    # se a request for get
    if request.method == 'GET':
        # pega todos os objetos do banco de dados referente aquela tabela
        snippets = Snippet.objects.all()
        # serializa os dados para ser viasualizado em json
        serializer = SnippetSerializer(snippets, many=True)
        # retorna os dados na request
        return JsonResponse(serializer.data, safe=False)

    # caso seja post
    elif request.method == 'POST':
        # Encapsula os dados no JSONParser
        data = JSONParser().parse(request)
        # passa pelo serializador para o python entender os dados
        serializer = SnippetSerializer(data=data)
        # verifica se os dados estão validos
        if serializer.data.is_valid():
            # caso sim, salva
            serializer.save()
            # retorna os dados e sucesso
            return JsonResponse(serializer.data, status=201)
        # caso nao seja válido retorna erro e status 400
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrive, Update, delete
    :param request:
    :param pk:
    :return:
    """
    try:
        # primeiro o sistema tenta encontrar o pk dentro do banco de dados
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        # retorna um erro de nao encontrado
        return HttpResponse(status=404)

    # se o método for get
    if request.method == 'GET':
        # serializa o snippet encontrado
        serializer = SnippetSerializer(snippet)
        # retorna o snippet encontrado
        return JsonResponse(serializer.data)

    # se o método for PUT(alterar)
    elif request.method == "POST":
        # recebe os dados enviado na request
        data = JSONParser().parse(request)
        # verifica o snippet encontrado e os dados recebido
        serializer = SnippetSerializer(snippet, data=data)
        # verifica se é valido o formulário
        if serializer.is_valid():
            # salva as alterações
            serializer.save()
            # retorna os dados
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # se for delete(deletar)
    elif request.method == "DELETE":
        # deleta do banco de dados
        snippet.delete()
        # retorna uma resposta que foi sucesso
        return HttpResponse(status=204)

