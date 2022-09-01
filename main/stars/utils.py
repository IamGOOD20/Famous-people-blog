from django.db.models import Count

from .models import *
site_map = [
      {'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'add_page'},
      {'title': 'Feedback', 'url_name': 'feedback'},

      ]

class DataMixen:
      paginate_by = 20
      def get_user_context(self, **kwargs):
            context = kwargs
            cats = Category.objects.annotate(Count('stars'))

            # hide addpage for not register users
            user_site_map = site_map.copy()
            if not self.request.user.is_authenticated:
                  user_site_map.pop(1)
            #

            context['site_map'] = user_site_map

            context['cats'] = cats
            if 'cat_selected' not in context:
                  context['cat_selected'] = 0
            return context