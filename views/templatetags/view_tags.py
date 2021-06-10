from avatar.utils import cache_result
from django.template.defaulttags import register
from django.template.loader import render_to_string


@cache_result()
@register.simple_tag
def view_card(view, **kwargs):

    context = {
        'view': view,
    }
    return render_to_string('views/view_card.html', context)