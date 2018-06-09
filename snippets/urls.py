from django.conf.urls import re_path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from testprint import views as testprint_views

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^schema/$', schema_view),
    re_path(r'^pdf/$', testprint_views.index),
    # re_path(r'^pdf/', testprint_views.proxy),
    re_path(r'^cups/$', testprint_views.cups),

]
