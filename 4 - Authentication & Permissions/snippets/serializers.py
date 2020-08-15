from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


# Usando ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    # criando um campo que recebera o username do usuario / acho que poderia adicionar o id dele
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'linenos', 'language', 'style', 'owner',]


class UserSerializer(serializers.ModelSerializer):
    # procura todos os snippet relacionado ao pk enviado se existir
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
