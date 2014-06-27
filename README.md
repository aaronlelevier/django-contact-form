# README

A simple Contact App for Django with one view for the Contact Form. The app stands by itself. It will
send the contact email to the ``DEFAULT_FROM_EMAIL`` set in ``settings.py`` if successful and redirect the User
to the Home page. Otherwise, the form will refresh showing what the User still needs to fill in, in order 
to send the Contact Form.

## Requirements
* Django 1.5+
* Python 3+ (may work on Python 2.7+ but haven't tested it yet)
* [django-crispy-forms](https://github.com/maraujop/django-crispy-forms)>=1.4.0

## Quickstart
Make sure that you have the above requirements set. Next add the following to your ``settings.py`` file:

* Add the App to your ``INSTALLED_APPS``
```python
INSTALLED_APPS += (
    'contact',
)
```

* Add the App to your ``urls.py``:
```python
urlpatterns = patterns('',
	# other urls
    url(r'contact/', include('contact.urls', namespace='contact')),
)
```

Add the following to ``settings.py``:

Your Site Name (or COMPANY_NAME as it is called in the settings) will appear in the email
```python
COMPANY_NAME = "LearnRealSQL"
```

The Contact App uses Bootstrap CSS by default, so **crispy-forms** is set to use this CSS
```python
CRISPY_TEMPLATE_PACK = "bootstrap3"
```

Email Settings
```python
# Any email backend that you want with the following setting
DEFAULT_FROM_EMAIL = "<email_address_that_your_contact_form_will_send_from"
```