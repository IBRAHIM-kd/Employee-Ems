from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from EMS.employee import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^employee/$', views.employee_list, name='employee_list'),
    url(r'^employee/create/$', views.employee_create, name='employee_create'),
    url(r'^employee/(?P<pk>\d+)/update/$', views.employee_update, name='employee_update'),
    url(r'^employee/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
