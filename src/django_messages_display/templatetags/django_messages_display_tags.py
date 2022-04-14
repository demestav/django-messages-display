from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("django_messages_display/close_button.html")
def close_button_element():
    include_close_button = getattr(
        settings, "DJANGO_MESSAGES_DISPLAY_CLOSE_BUTTON", None
    )

    return {"include_close_button": include_close_button}
