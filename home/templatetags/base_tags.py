from django import template
from wagtail.core.models import Site

from home.blocks import MapBlock
from home.snippets_models import Header, Footer

register = template.Library()


@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'request': context['request'],
        'header': Header.objects.first(),
    }


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
    }


# @register.inclusion_tag('home/tags/product_cards.html', takes_context=True)
# def product_card_tag(context):
#     return {
#         'request': context['request'],
#         'product_card': ProductCard.objects.all(),
#     }
#
#
# @register.inclusion_tag('home/tags/event_news.html', takes_context=True)
# def event_news_tag(context):
#     return {
#         'request': context['request'],
#         'event_news_snip': EventNewsPages.objects.all(),
#     }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context['request']).root_page


# ----------------------------------------------------------------------------------------------------------------------
def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return (current_page.url_path.startswith(page.url_path) if current_page else False)


# ----------------------------------------------------------------------------------------------------------------------


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
        menuitem.children = menuitem.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.simple_tag
def counter(count):
    count += 1
    return count


@register.simple_tag
def counter_two(count_two):
    count_two += 1
    return count_two


@register.simple_tag
def doc_icon(url_doc):

    sample_doc = ['pdf', 'txt', 'xls', 'zip']
    url_doc_list = url_doc.lower().split('.')
    if url_doc_list[-1] in sample_doc:
        file_type = 'file-' + url_doc_list[-1]
    else:
        file_type = 'file-txt'

    return file_type


@register.simple_tag
def doc_patch(url_doc):

    url_doc_list = url_doc.split('/')
    url_doc_list.pop(-2)
    url = '/'.join(url_doc_list)
    return url
