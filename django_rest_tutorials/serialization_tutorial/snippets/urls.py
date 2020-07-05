from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from snippets import views

# suffix처리기 포함
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
