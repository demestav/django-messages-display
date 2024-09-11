# django-messages-display
Display messages from django.contrib.messages as notifications in the browser.

## Setup
Install the package using `pip`:

```shell
python -m pip install django-messages-display
```

Add it to the installed apps of your project:
```python
INSTALLED_APPS = [
    ...
    "django_messages_display",
    ...
]
```

## How to use
1. Load the template tag in your template:
   ```
   {% load django_messages_display %}
   ```

2. Use the `django_messages_display` tag where you want the notifications to appear:
   ```
   {% django_messages_display %}
   ```
   A good place to add this is before the closing body tag `</body>`.

3. Load the CSS for the styling to apply:
   ```
   {% load static %}
   ...
   <head>
      ...
      <link rel="stylesheet" href="{% static 'django_messages_display/django_messages_display.css' %}">
   </head>
   ```

### Example
It is convenient to integrate django-messages-display in your base template:

```html
<!-- base.html -->
{% load static %}
{% load django_messages_display %}
...
<head>
   ...
   <link rel="stylesheet" href="{% static 'django_messages_display/django_messages_display.css' %}">
</head>
...
{% django_messages_display %}
</body>
...
```

## Configuration
To include a close button for each message, add the following to your Django settings:

```python
DJANGO_MESSAGES_DISPLAY_CLOSE_BUTTON = True
```

To change message display delay from default 5000ms, add the following to your Django settings:
```python
DJANGO_MESSAGES_DISPLAY_DELAY = 10000
```


## Accessibility
The notifications have the relevant attributes so that screen readers announce each one without interrupting the user's flow.
Even though the notifications visually disappear after a certain amount of time, they remain in the document to be accessible by screen readers on demand.

The colors used for the notifications meet the WCAG 2.1 AA contrast levels.