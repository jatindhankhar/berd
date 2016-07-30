from django import template
register = template.Library()

@register.filter(name='get_tag_names')
def get_tag_names(tag_object):
    return [tag.name for tag in tag_object]
