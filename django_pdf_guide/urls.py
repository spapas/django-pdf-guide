from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from books import urls as books_urls
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='book_index') ),
    path('books/', include(books_urls, ) ),
    path('admin/', admin.site.urls ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
