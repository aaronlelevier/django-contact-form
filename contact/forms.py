from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div

from .models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact  
		fields = ('name', 'email', 'subject', 'message',)
		widgets = {
			'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
		}

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-lg-2'
	helper.field_class = 'col-lg-8'
	helper.layout = Layout(
		Fieldset(
			'', 'name', 'email', 'subject', 'message',
		),
		Div(
			Submit('submit', 'Submit', css_class='btn-primary'),
			css_class='col-lg-offset-2',
		)
	)