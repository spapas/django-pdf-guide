from django.urls import include, path
from django.contrib import admin

import books.views

urlpatterns = [
    path('', books.views.BookIndexTemplateView.as_view(), name='book_index',),
    path('books_plain_old_view', books.views.books_plain_old_view, name='books_plain_old_view',),
    path('books_plain_old_view_content_disp', books.views.books_plain_old_view_content_disp, name='books_plain_old_view_content_disp',),
    path('book_pdf_detail_view/<int:pk>/', books.views.BookPdfDetailView.as_view(), name='book_pdf_detail_view',),
    path('book_pdf_list_view', books.views.BookPdfListView.as_view(), name='book_pdf_list_view',),
    path('book_list_ex', books.views.BookExPdfListView.as_view(), name='book_list_ex',),
    path('cover_book_list', books.views.CoverBookPdfListView.as_view(), name='cover_book_list',),
    path('book_pdf_card_list', books.views.BookCardPdfListView.as_view(), name='book_pdf_card_list',),
]
