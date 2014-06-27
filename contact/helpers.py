from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def contact_email(name, email, email_subject, message):
	subject, from_email, to = '{0}: Contact Email from {1}'.format(settings.COMPANY_NAME, name), settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_FROM_EMAIL
	text_content = 'Name: {0}; Email {1}; Subject {2}; Message {3}'.format(name, email, email_subject, message)
	html_content = render_to_string('contact/html_contact_email.html', {'name':name, 'email':email, 'subject':email_subject, 'message':message})
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	return msg 	