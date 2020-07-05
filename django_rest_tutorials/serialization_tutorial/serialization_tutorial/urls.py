from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Default login, logout view(browsable PI)
]
