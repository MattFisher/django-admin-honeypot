try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('admin_honeypot.views',
    url(r'^.*$', 'admin_honeypot', name='admin_honeypot'),
)
