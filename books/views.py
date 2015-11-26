from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf

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
    def render_to_response(self, context, **response_kwargs):
        context=self.get_context_data()
        template=self.get_template_names()[0]
        resp = HttpResponse(content_type='application/pdf')
        result = generate_pdf(template, file_object=resp, context=context)
        return result


class BookPdfListView(PdfResponseMixin, ListView):
    context_object_name = 'books'
    model = Book


class BookPdfDetailView(PdfResponseMixin, DetailView):
        context_object_name = 'book'
        model = Book


class BookExPdfListView(PdfResponseMixin, ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'books/book_list_ex.html'
