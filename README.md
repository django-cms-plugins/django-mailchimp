Simple Mailchimp support for Django
====================================

just a simple sign up form for mailchimp newsletters

Requirements
--------------

* Django (checked with 1.4+)
* mailsnake
* classytags

Installation
-------------

Add `mailchimp` to your `INSTALLED_APPS`, and set two settings variables:

Usage
------

It defines a single template tag `mailchimp_subscribe_form` that you can call with your mailchimp list id to show a subscribe form for it.

How to integrate it with django-cms
------------------------------------

Create a `cms_plugins.py` file, and add the following to it:

```
from mailchimp.forms import SubscribeForm

class MailchimpPlugin(CMSPluginBase):
	model = SignupFormPlugin
	name = _('Mailchimp Signup Form')
	render_template = 'mailchimp/subscribe.html'

	def render(self, context, instance, placeholder):
		subscribeForm = SubscribeForm(initial={'list_id': instance.list_id})
		return context.update({
			'csrf_token': context['csrf_token'],
			'form': subscribeForm
			})
plugin_pool.register_plugin(MailchimpPlugin)
```

Add to your `urls.py`:

```
url(r'^maillist/', include('mailchimp.urls', namespace='mailchimp')),
```

Add to your `models.py`

```
from cms.models import CMSPlugin

class SignupFormPlugin(CMSPlugin):
	list_id = models.CharField(max_length=30)

	def __unicode__(self):
		return self.list_id
```

Websites using this app
------------------------

* [Jalagati Jóga Egyesület](http://jalagat.hu)