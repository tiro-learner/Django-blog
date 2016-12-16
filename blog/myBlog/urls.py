from django.conf.urls import url
from . import views
import django.views.static
from blog import settings
app_name = 'myBlog'
urlpatterns = [
    url(r'^$', views.page_view, name='index'),
    url(r'^pages/(?P<page>[0-9]+)/$', views.page_view, name='pages'),
    url(r'^tags/$', views.tags_view, name='tags'),
    url(r'^categories/$', views.categories_view, name='categories'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.article_view, name='article'),
    url(r'^uploads/media/(?P<path>.*)/$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
]