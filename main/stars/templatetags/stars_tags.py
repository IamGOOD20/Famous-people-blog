from django import template
from stars.models import *


register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
      if filter is None:
            return Category.objects.all()
      else:
            return Category.objects.get(pk=filter)


@register.inclusion_tag('stars/list_categories.html')
def show_categories(sort=None, cat_selected=0):
      if not sort:
            cats = Category.objects.all()
      else:
            cats = Category.objects.order_by(sort)

      return {'cats': cats, 'cat_selected': cat_selected}
