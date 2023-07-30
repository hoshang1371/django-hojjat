# importing the necessary libraries
from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from xhtml2pdf import pisa  
from weasyprint import HTML, CSS
from pdfkit import pdfkit
from django.contrib.sites.shortcuts import get_current_site
import os
from django.conf import settings

sample_data = [{'url': 'http://www.google.com/', 'title': 'گوگل'},
                {'url': 'http://www.yahoo.com/fa/', 'title': 'یاهو'},
                {'url': 'http://www.amazon.com/', 'title': 'آمازون'}]


# defining the function to convert an HTML file to a PDF file
def html_to_pdf(request,template_src, context_dict={}):
    template = get_template(template_src)
    domain= request.build_absolute_uri('/')[:-1]

    css1 = os.path.join(settings.STATIC_ROOT, 'css', 'post_order.css')
    print('css1',css1)

    # html  = template.render({
    #     'order_details': context_dict,
    #     'domain' : domain,
    #     })
    context_dict['domain'] = domain
    html  = template.render(
        context_dict,
        )
    # print('domain=',d)
    options = {'encoding': "UTF-8", 'quiet': ''}

    bytes_array = pdfkit.PDFKit(html, 'string', options=options).to_pdf()

    return HttpResponse(bytes_array, content_type='application/pdf')
