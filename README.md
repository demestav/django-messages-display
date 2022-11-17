# django-messages-display
Display messages from django.contrib.messages as notifications in the browser.

## Setup
Install package using `pip`:

```shell
python -m pip install django-messages-display
```

Add it to the installed apps:
```python
INSTALLED_APPS = [
    ...
    "django_messages_display",
    ...
]
```

## How to use
Include the package template in templates where notifications are needed. If site-wide notifications apply for the whole site, it is convenient to add it to the base template, if there is one.

```
{% include 'django_messages_display/django_messages_display.html' %}
```

Further, for the styling to apply, the CSS should be loaded:
```
{% load static %}
...
<head>
    ...
    <link rel="stylesheet" href="{% static 'django_messages_display/django_messages_display.css' %}">
</head>
```

## Accessibility
Notifications have the relevant attributes, so that the screen reader announces each one without interrupting the users' flow.
Even though visually the notifications disappear after a certain amount of time, they remain in the document in order to be accessible by the screen reader on demand.

The colors used for the notifications, meet the WCAG (2.1) AA contrast levels.