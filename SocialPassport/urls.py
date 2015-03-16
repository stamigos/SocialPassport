from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from django.http import request
from sp.models import Squad, Student
from sp.views import SquadsListView
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sp.views.squad_list',
        {'template_name': 'sp/squad_list.html'},
        name='index'),
    #url(r'^$', SquadsListView.as_view(), squad_info, name='index'),
    url(r'^(?P<squad_name>\d+)/$', 'sp.views.squad_detail',
        {'template_name': 'sp/student_list.html'},
        name='squad'),
    url(r'^(?P<squad_name>\d+)/(?P<student_id>\d+)/$', 'sp.views.student_detail',
        {'template_name': 'sp/student_detail.html'}, name='student_detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

