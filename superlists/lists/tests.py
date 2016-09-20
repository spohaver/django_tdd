from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page


class SmokeTest(TestCase):

    def test_root_url(self):
        # Is the home_page there?
        found = resolve('/')
        self.assertEqual(found.func, home_page)
