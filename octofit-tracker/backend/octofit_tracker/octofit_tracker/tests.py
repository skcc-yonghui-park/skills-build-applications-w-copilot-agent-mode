from django.test import SimpleTestCase
from django.urls import reverse

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout


class CollectionModelTableTests(SimpleTestCase):
    def test_db_table_mappings(self):
        self.assertEqual(Team._meta.db_table, 'teams')
        self.assertEqual(UserProfile._meta.db_table, 'users')
        self.assertEqual(Activity._meta.db_table, 'activities')
        self.assertEqual(Leaderboard._meta.db_table, 'leaderboard')
        self.assertEqual(Workout._meta.db_table, 'workouts')


class ApiRouteTests(SimpleTestCase):
    def test_api_root_reverse(self):
        self.assertEqual(reverse('api-root'), '/api/')
