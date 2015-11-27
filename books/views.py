import os, StringIO

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf

from PyPDF2 import PdfFileMerger

from books.models import Book

class BookIndexTemplateView(TemplateView):
    template_name = 'book_index.html'


def books_plain_old_view(request):
    resp = HttpResponse(content_type='application/pdf')
    context = {
        'books': Book.objects.all()
    }
    result = generate_pdf('books_plain_old_view.html', file_object=resp, context=context)
    return result


def books_plain_old_view_content_disp(request):
    resp = HttpResponse(content_type='application/pdf')
    resp['Content-Disposition'] = 'attachment; filename="output.pdf"'
    context = {
        'books': Book.objects.all()
    }
    result = generate_pdf('books_plain_old_view.html', file_object=resp, context=context)
    return result


class PdfResponseMixin(object, ):
    def write_pdf(self, file_object, ):
        context = self.get_context_data()
        template = self.get_template_names()[0]
        generate_pdf(template, file_object=file_object, context=context)

    def render_to_response(self, context, **response_kwargs):
        resp = HttpResponse(content_type='application/pdf')
        self.write_pdf(resp)
        return resp
        

class CoverPdfResponseMixin(PdfResponseMixin, ):
    cover_pdf = None
    
    def render_to_response(self, context, **response_kwargs):
        merger = PdfFileMerger()
        merger.append(open(self.cover_pdf, "rb"))
        
        pdf_fo = StringIO.StringIO()
        self.write_pdf(pdf_fo)
        merger.append(pdf_fo)
        
        resp = HttpResponse(content_type='application/pdf')
        merger.write(resp)
        return resp


class BookPdfListView(PdfResponseMixin, ListView):
    context_object_name = 'books'
    model = Book


class BookPdfDetailView(PdfResponseMixin, DetailView):
    context_object_name = 'book'
    model = Book
    
    
class BookCardPdfListView(PdfResponseMixin, ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'card_layout.html'

class BookExPdfListView(PdfResponseMixin, ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'books/book_list_ex.html'

    
class CoverBookPdfListView(CoverPdfResponseMixin, ListView):
    context_object_name = 'books'
    cover_pdf = os.path.join(settings.STATIC_ROOT, 'cover.pdf')
    model = Book
    template_name = 'books/book_list_ex.html'
