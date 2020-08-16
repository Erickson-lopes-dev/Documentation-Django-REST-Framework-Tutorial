from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetGenericsList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippentGenericsDetail.as_view(), name='snippet-detail'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight')
]
