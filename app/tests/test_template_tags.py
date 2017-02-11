from datetime import date
from django.test.testcases import TestCase

from app.templatetags.custom_tags import age


class CustomTemplateTagsTests(TestCase):
    def test_age_filter_with_empty_birthday(self):
        """
        Age filter should return empty string because birthday param is None
        """

        birthday = None
        self.assertEqual(age(birthday), '')

    def test_age_filter_with_future_birthday(self):
        """
        Age filter should return 0 for future birthday
        """

        today = date.today()
        birthday = date(year=today.year + 1, month=today.month, day=today.day)
        self.assertEqual(age(birthday), 0)

    def test_age_filter_with_past_birthday(self):
        """
        Age filter should return greater than 0 for past birthday
        """

        birthday = date(year=1990, month=3, day=15)
        self.assertGreater(age(birthday), 0)

    def test_age_filter_with_today_birthday(self):
        """
        Age filter should return a valid age for if today is birthday
        """

        today = date.today()
        birthday = date(year=today.year - 5, month=today.month, day=today.day)
        self.assertEqual(age(birthday), 5)
