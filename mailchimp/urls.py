"""Defaults urls for the Zinnia project"""
from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    '',
    url(r'^subscribe/$', 'mailchimp.views.subscribe', name='subscribe'),
    url(r'^unsubscribe/$', 'mailchimp.views.unsubscribe', name='unsubscribe'),
    url(r'^subscribe/success/$', direct_to_template, {'template': 'mailchimp/successful_subscription.html'}, name='subscribe_success'),
    url(r'^subscribe/failure/$', direct_to_template, {'template': 'mailchimp/failed_subscription.html'}, name='subscribe_failed'),
)
