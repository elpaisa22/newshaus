from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.default_view, name="default_view"),
    url(r'^categoria/(?P<category_name>[\w\-]+)$', views.post_by_category, name="post_by_category"),
    url(r'^articulo/(?P<pk>[0-9]+),(?P<slug>[-\w\d]+)$', views.post_detail, name='post_detail'),
    url(r'^buscar$', views.search_text, name='article_search_list_view'),
    url(r'^pagina/(?P<page_name>[\w\-]+)$', views.generic_page_view, name='generic_page_view')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
