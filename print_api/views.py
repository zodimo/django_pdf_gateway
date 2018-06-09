from print_api.serializers import PdfGenSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from print_api.models import Pdfgen

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from rest_framework import renderers

from rest_framework import viewsets
from rest_framework.decorators import action


from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.http.response import HttpResponse, HttpResponseGone, HttpResponseNotFound
from rest_framework.views import APIView




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pdfgen': reverse('pdfgen', request=request, format=format),
        # 'apdfgen': reverse('apdfgen', request=request, format=format)
    })


class PdfgenList(generics.ListCreateAPIView):
    queryset = Pdfgen.objects.all()
    serializer_class = PdfGenSerializer

class PdfgenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdfgen.objects.all()
    serializer_class = PdfGenSerializer

def PdfgenDownload(request,pk):
    try:
        pdfgen = Pdfgen.objects.get(pk=pk)
    except Pdfgen.DoesNotExist:
        return HttpResponseNotFound()

    if pdfgen.rendered_file:
        return HttpResponse(pdfgen.rendered_file,content_type='application/pdf')
    else:
        return HttpResponseGone()