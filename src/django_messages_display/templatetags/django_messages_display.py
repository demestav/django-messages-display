from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def django_messages_display(context):
    include_close_button = getattr(
        settings, "DJANGO_MESSAGES_DISPLAY_CLOSE_BUTTON", None
    )

    delay = getattr(
        settings, "DJANGO_MESSAGES_DISPLAY_DELAY", None
    )
    messages = context.get('messages', [])
    
    render_context = {
        "include_close_button": include_close_button,
        "delay": delay,
        "messages": messages,
    }
    
    return render_to_string(
        "django_messages_display/django_messages_display.html", render_context
    )
