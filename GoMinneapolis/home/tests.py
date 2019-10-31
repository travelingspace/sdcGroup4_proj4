from django.test import TestCase
from models import yelpRestaurants

# Create your tests here.

class DictLength(TestCase):

    def test_length_of_list_made_by_yelp_api(self):
        test_searchYelp = {}
        yelpRestaurants.searchYelp(self, 55414)
        test_list_length = len(test_searchYelp)
        self.assertEquals(test_list_length, 20)