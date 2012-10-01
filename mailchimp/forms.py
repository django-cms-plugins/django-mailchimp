from django import forms
from django.conf import settings

from mailsnake import MailSnake
from mailsnake.exceptions import *

ms = MailSnake(settings.MAILCHIMP_API_KEY)

class SubscribeForm(forms.Form):
	list_id = forms.CharField(widget=forms.HiddenInput)
	name = forms.CharField()
	email = forms.EmailField()

	def save(self):
		try:
		    ms.ping() # returns "Everything's Chimpy!"
		except MailSnakeException:
		    return False
		except ListAlreadySubscribedException:
			# we could handle the response in the view
			return False
		except:
			return False
		else:
			return ms.listSubscribe(id=self.cleaned_data['list_id'],
				email_address=self.cleaned_data['email'],
				merge_vars={'NAME': self.cleaned_data['name']},
				double_optin=False, send_welcome=True)    