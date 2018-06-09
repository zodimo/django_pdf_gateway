from django.shortcuts import render
from django.http.response import HttpResponse
import testprint.pdf_test
import urllib.request
import http.client
import pdfkit
import weasyprint
import reportlab
# from reportlab.pdfgen import
from weasyprint import HTML, CSS

import xhtml2pdf.pisa as pisa
import io


from django.views.decorators.csrf import csrf_exempt



PROXY_BASE_URL='http://www.oldbaileyonline.org'

# Create your views here.
#
def index(request):

    webContent='''
    <html>
    <head>
    <style>
body {
    background-color: linen;
}

h1 {
    color: maroon;
    margin-left: 40px;
} 
</style>
    </head>
    <body>
        <h1>Hi Superman</h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Cumulonimbus_Clouds_seen_from_SCTEX.jpg" alt="Flowers in Chania">
    </body>
    </html>
    
    
    '''

    # url_string='https://www.google.co.za/search?q=cups+pdf&oq=cups+pdf&aqs=chrome..69i57j35i39j0l4.5160j0j7&sourceid=chrome&ie=UTF-8'
    url_string='https://www.google.co.za'
    # url_string='http://www.munsoft.co.za'
    # url_string='http://www.itna.co.za'
    # url_string='https://www.webstandards.org/files/acid2/test.html#top'
    url_string='https://www.w3.org/TR/CSS21/intro.html'
    pdf=None

    # url_string = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
    try:
        response = urllib.request.urlopen(url_string)
        response_info=response.info()  #type:  http.client.HTTPMessage
        charset=response_info.get('Content-Type').split(' ')[1].split('=')[1]
        webContent = response.read().decode(charset)
    except Exception as e:
        print(type(e))
    # print(response.info())

    pdf_obj = HTML(string=webContent.encode("UTF-8"), media_type='print')
    # pdf_obj = HTML(url=url_string,media_type='print')
    page_css='''
    @page {
        margin: 3cm 2cm;
        padding-left: 1.5cm;
        size: A4 landscape;
    }
    '''

    pdf=pdf_obj.write_pdf()
    # stylesheets=[CSS(string=page_css)]
    # print(webContent)

    # options={
    #     'orientation':'landscape',
    #     'page-size':'A4',
    #     'disable-smart-shrinking': True
    # }
    #
    # try:
    #     # with urllib.request.urlopen(url_string) as f:
    #     #     pdf=pdfkit.from_file(f, False)
    #     pdf = pdfkit.from_url(url_string, False,options)
    # except Exception as e:
    #     print(e)
    #     pdf = pdfkit.from_string(str(html), False,options)

    # html = response.read()


    # html=url_content_handle.encode('utf-8')
    # pdf = pdfkit.from_url(url, False)


    return HttpResponse(pdf,content_type='application/pdf')
    # return HttpResponse(webContent)

def cups(request):
    import cups
    cups_pdf_uri='cups-pdf:/'
    cups_pdf_printer=None
    conn = cups.Connection()

    printers = conn.getPrinters()
    for printer in printers:
        if printers[printer]["device-uri"] == cups_pdf_uri:
            cups_pdf_printer=printers[printer]

    print(cups_pdf_printer)
    if(cups_pdf_printer):
        printer_name=str(cups_pdf_printer['printer-info']).replace(' ','_')


        print(conn.printTestPage(printer_name))



    return HttpResponse('hello, check the console.')

@csrf_exempt
def proxy(request):

    print('Proxying....')
    orig_request=request.get_full_path()
    request_path=str(orig_request).replace('/pdf','')

    url = ''.join([PROXY_BASE_URL,request_path])

    response = urllib.request.urlopen(url)
    http_message = response.info() #type:  http.client.HTTPMessage
        # .gettype()
    # message = http_message.getplist()
    # webContent =response

    print(http_message.get('Content-Type'))
    # print(http_message)


    # return HttpResponse(response.read(),content_type=http_message.get('Content-Type'))
    return HttpResponse('')

# def get_printers():
#
#
# def create_printer():






