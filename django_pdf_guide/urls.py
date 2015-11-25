from django.conf.urls import include, url
from django.contrib import admin
from books import urls as books_urls

urlpatterns = [
    url(r'^books/', include(books_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
