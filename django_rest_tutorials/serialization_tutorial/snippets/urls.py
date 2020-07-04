from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# url에 .json, .html, .api등을 추가하여 타입을 요청할 수 있다.
urlpatterns = format_suffix_patterns(urlpatterns)