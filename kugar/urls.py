from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kugar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('kugar_webapp.urls')),
]
