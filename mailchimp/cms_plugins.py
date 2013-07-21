from django.template import Context
from django.utils.translation import ugettext as _

from .forms import SubscribeForm
from .models import SignupFormPlugin

class MailchimpPlugin(CMSPluginBase):
    model = SignupFormPlugin
    name = _('Mailchimp Signup Form')
    render_template = 'mailchimp/subscribe.html'

    def render(self, context, instance, placeholder):
        subscribeForm = SubscribeForm(initial={'list_id': instance.list_id})
        return Context({
            'csrf_token': context['csrf_token'],
            'form': subscribeForm
            })
plugin_pool.register_plugin(MailchimpPlugin)