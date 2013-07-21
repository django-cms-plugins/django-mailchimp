from django.db import models

try:
    from cms.models import CMSPlugin

    class SignupFormPlugin(CMSPlugin):
        list_id = models.CharField(max_length=30)

        def __unicode__(self):
            return self.list_id
except ImportError:
    pass