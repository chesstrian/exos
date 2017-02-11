from datetime import date
from django.test.testcases import TestCase

from app.models import Profile


class UserProfilePropertiesTest(TestCase):
    def test_eligible_property_empty_value(self):
        """
        eligible property should return '' if no age
        """

        profile = Profile(birthday=None)
        self.assertEqual(profile.eligible, '')

    def test_eligible_property_allowed_value(self):
        """
        eligible property should return 'allowed' if age > 13
        """

        profile = Profile(birthday=date(year=1990, month=3, day=15))
        self.assertEqual(profile.eligible, 'allowed')

    def test_eligible_property_blocked_value(self):
        """
        eligible property should return 'blocked' if age <= 13
        """

        profile = Profile(birthday=date(year=2004, month=2, day=1))
        self.assertEqual(profile.eligible, 'blocked')

    def test_bizz_fuzz_property_not_divisible_value(self):
        """
        bizz_fuzz property should return same number if it's not divisible by 3 and 5
        """

        profile = Profile(random_number=17)
        self.assertEqual(profile.bizz_fuzz, 17)

    def test_bizz_fuzz_property_divisible_by_3_value(self):
        """
        bizz_fuzz property should return 'Bizz' if it's divisible by 3 but not by 5
        """

        profile = Profile(random_number=12)
        self.assertEqual(profile.bizz_fuzz, 'Bizz')

    def test_bizz_fuzz_property_divisible_by_5_value(self):
        """
        bizz_fuzz property should return 'Fuzz' if it's divisible by 5 but not by 3
        """

        profile = Profile(random_number=25)
        self.assertEqual(profile.bizz_fuzz, 'Fuzz')

    def test_bizz_fuzz_property_divisible_by_both_value(self):
        """
        bizz_fuzz property should return 'BizzFuzz if it's divisible by 3 and 5
        """

        profile = Profile(random_number=15)
        self.assertEqual(profile.bizz_fuzz, 'BizzFuzz')
