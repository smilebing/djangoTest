from django.conf.urls import url
from blog.views import RSSFeed

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^blog/archives/$', views.archives, name='archives'),
    url(r'^blog/aboutme/$', views.about_me, name='about_me'),
    url(r'^blog/tag/(?P<tag>\w*)/$', views.search_tag, name='search_tag'),
    url(r'^blog/search/$', views.blog_search, name='search'),
    url(r'^feed/$',RSSFeed(), name="RSS"),  # 新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
]
