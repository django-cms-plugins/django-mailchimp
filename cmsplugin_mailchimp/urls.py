"""Defaults urls for the Zinnia project"""
from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic.simple import direct_to_template
from .views import subscribe, unsubscribe

urlpatterns = patterns(
    '',
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^unsubscribe/$', unsubscribe, name='unsubscribe'),
    url(r'^subscribe/success/$', direct_to_template, {'template': 'cmsplugin_mailchimp/successful_subscription.html'}, name='subscribe_success'),
    url(r'^subscribe/failure/$', direct_to_template, {'template': 'cmsplugin_mailchimp/failed_subscription.html'}, name='subscribe_failed'),
)
