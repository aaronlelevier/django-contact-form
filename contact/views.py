from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages

from .models import Contact
from .forms import ContactForm
from .helpers import contact_email


class ContactView(FormView):
	"""
	ContactForm is a ModelForm
	"""
	template_name = 'contact/contact.html'
	form_class = ContactForm
	success_url = reverse_lazy('blog:index')

	def form_valid(self, form):
		cd = form.cleaned_data
		contact = Contact.objects.create(**form.cleaned_data)
		if contact:
			# send contact email
			msg = contact_email(name=cd['name'], email=cd['email'], 
					email_subject=cd['subject'], message=cd['message'])
			msg.send()
			# Add success message 
			msg = "Your contact email has been successfully sent.\
			We look forward to speaking with you."
			messages.info(self.request, msg)
		return super(ContactView, self).form_valid(form)