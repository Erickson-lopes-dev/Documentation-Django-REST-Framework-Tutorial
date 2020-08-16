from rest_framework import permissions


# permissão apenas se o uy
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Permissão apenas para o criador do objeto
    """
    def has_object_permission(self, request, view, obj):
        # Permissões de leitura são permitidas a qualquer solicitação,
        # portanto, sempre permitiremos solicitações GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissões de gravação são permitidas apenas para o proprietário do snippet.
        return obj.owner == request.user
