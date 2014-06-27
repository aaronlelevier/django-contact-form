from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact


class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	search_fields = ['name', 'email']
	list_display = ('name', 'email', 'subject',)
	readonly_fields = ('created',)
	fieldsets = [
		('Info',				{'fields': ['name', 'email']}),
		('Message', 	 		{'fields': ['subject', 'message']}),
		('Auto Fields',			{'fields': ['created']})
	]

	
admin.site.register(Contact, ContactAdmin)