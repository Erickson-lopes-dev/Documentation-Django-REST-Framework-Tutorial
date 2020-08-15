from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippentDetail.as_view()),

    path('snippets/mixins/', views.SnippetMixinsList.as_view()),
    path('snippets/mixins/<int:pk>/', views.SnippentMixinsDetail.as_view()),

    path('snippets/generic/', views.SnippetGenericsList.as_view()),
    path('snippets/generic/<int:pk>/', views.SnippentGenericsDetail.as_view()),
]
