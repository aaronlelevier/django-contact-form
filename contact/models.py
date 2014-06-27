from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.urlresolvers import reverse


class Contact(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(_("Name"), max_length=100)
	email = models.EmailField(_("Email"), max_length=100)
	subject = models.CharField(_("Subject"), max_length=200)
	message = models.TextField(_("Message"), max_length=2000)

	def __str__(self):
		return u"%s : %s" % (self.name, self.email)

	def get_absolute_url(self):
		return reverse('contact:contact')