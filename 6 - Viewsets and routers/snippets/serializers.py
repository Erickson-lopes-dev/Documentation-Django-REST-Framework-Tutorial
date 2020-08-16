from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


# Usando ModelSerializer
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # criando um campo que recebera o username do usuario / acho que poderia adicionar o id dele
    owner = serializers.ReadOnlyField(source='owner.username')
    # cria um campo com a url do item
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight')

    class Meta:
        model = Snippet
        # passando url com os atributos
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # procura todos os snippet relacionado ao pk enviado se existir / retornando a url dele
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        # passando url com os atributos
        fields = ['url', 'id', 'username', 'snippets']
