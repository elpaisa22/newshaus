from django import template
register = template.Library()

@register.filter
def index(list, i):
    if (len(list) > i):
        return list[int(i)]
    else:
        return None
