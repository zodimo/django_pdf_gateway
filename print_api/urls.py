from django.conf.urls import re_path, include
from rest_framework.routers import DefaultRouter
from print_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    # re_path(r'^', views.api_root),
    re_path(r'^pdfgen/$', views.PdfgenList.as_view()),
    re_path(r'^pdfgen/(?P<pk>[0-9]+)/$', views.PdfgenDetail.as_view()),
    re_path(r'^pdfgen/(?P<pk>[0-9]+)/download$', views.PdfgenDownload),

]


#
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
