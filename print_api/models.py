from django.db import models
from weasyprint import HTML, CSS
import urllib.request
from django.core.exceptions import ValidationError

# Create your models here.

PDF_ADDITIONAL_CSS='''
    @page {
        size: A4 portrait;
    }
    @viewport {
      width: 1024;
    }
'''

class Pdfgen(models.Model):
    name=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    website=models.URLField(blank=True)
    rendered_file=models.BinaryField(blank=True)

    download_link=None



    def save(self, *args, **kwargs):
        pdf=None
        pdf_obj=None

        if self.content is not '':
            pdf_obj = HTML(string=str(self.content).encode("UTF-8"))
        elif self.website  is not '':
            pdf_obj = HTML(url=self.website)

        if pdf_obj is not None:
            pdf=pdf_obj.write_pdf(stylesheets=[CSS(string=PDF_ADDITIONAL_CSS)])

        self.rendered_file=pdf

        super(Pdfgen, self).save(*args, **kwargs)







