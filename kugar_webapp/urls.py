from django.conf.urls import patterns, url
from kugar_webapp import views


urlpatterns = patterns('',

    url(r'^$', views.main, name='main'),
    url(r'results/$', views.results, name='results'),
    url(r'^termsandconditions/$', views.terms_and_conditions, name='terms_and_conditions'),
)

