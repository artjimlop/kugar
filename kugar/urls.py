from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kugar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('kugar_webapp.urls')),
]

# Solución a los estáticos en Heroku
# Mil gracias: http://stackoverflow.com/questions/9047054/heroku-handling-static-files-in-django-app
# if settings.DEBUG ??
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )