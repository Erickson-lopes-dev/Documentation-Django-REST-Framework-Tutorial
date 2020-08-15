from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetGenericsList.as_view()),
    path('snippets/<int:pk>/', views.SnippentGenericsDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]
