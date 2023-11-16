from django import template
from django.urls import reverse
from django.utils.html import mark_safe
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info
    print('current_path: ',menu_name)
    menu_items = MenuItem.objects.filter(url=menu_name).prefetch_related('children')
    menu_html = '<ul>'
    if bool(menu_items):
        for item in menu_items:
            menu_html += '<li>'
            if item.url == current_path:
                menu_html += f'<a href="{item.url}" class="active">{item.name}</a>'
            else:
                menu_html += f'<a href="{item.url}">{item.name}</a>'
            if item.children.exists():
                menu_html += '<ul>'
                for child in item.children.all():
                    menu_html += '<li>'
                    if child.url == current_path:
                        menu_html += f'<a href="{child.url}" class="active">{child.name}</a>'
                    else:
                        menu_html += f'<a href="{child.url}">{child.name}</a>'
                    menu_html += '</li>'
                menu_html += '</ul>'
            menu_html += '</li>'
    else:
        menu_items= MenuItem.objects.filter(parent_item=None)
        for item in menu_items:
            menu_html += '<li>'
            menu_html += f'<a href="{item.url}">{item.name}</a>'
            menu_html += '</li>'
    menu_html += '</ul>'
    return mark_safe(menu_html)