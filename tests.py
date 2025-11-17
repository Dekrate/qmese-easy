import unittest
from datetime import date, timedelta
from user_manager_a import UserManager


class TestUserManagerA(unittest.TestCase):

    def setUp(self):
        self.manager = UserManager()
        # Add test users
        self.manager.add_user("John Smith", "john@example.com", "1990-05-15")
        self.manager.add_user("Anna Johnson", "anna@example.com", "2005-08-20")
        self.manager.add_user("Peter Wilson", "peter@example.com", "1955-12-01")
        self.manager.add_user("Maria Brown", "maria@example.com", "2010-03-10")

    def test_calculate_age_adult(self):
        """Test age calculation for adult"""
        age = self.manager.calculate_age("1990-05-15")
        expected_age = date.today().year - 1990
        # Account for whether birthday has occurred this year
        if date.today() < date(date.today().year, 5, 15):
            expected_age -= 1
        self.assertEqual(age, expected_age)

    def test_calculate_age_child(self):
        """Test age calculation for child"""
        age = self.manager.calculate_age("2010-03-10")
        expected_age = date.today().year - 2010
        if date.today() < date(date.today().year, 3, 10):
            expected_age -= 1
        self.assertEqual(age, expected_age)

    def test_calculate_age_future_date(self):
        """Test age calculation for future date"""
        future_date = (date.today() + timedelta(days=365)).strftime("%Y-%m-%d")
        age = self.manager.calculate_age(future_date)
        self.assertEqual(age, 0)  # Or appropriate error handling

    def test_get_age_based_discount_child(self):
        """Test discount for child (0-17 years)"""
        discount = self.manager.get_age_based_discount("anna@example.com")
        self.assertEqual(discount, 20)

    def test_get_age_based_discount_adult(self):
        """Test discount for adult (18-64 years)"""
        discount = self.manager.get_age_based_discount("john@example.com")
        self.assertEqual(discount, 0)

    def test_get_age_based_discount_senior(self):
        """Test discount for senior (65+ years)"""
        discount = self.manager.get_age_based_discount("peter@example.com")
        self.assertEqual(discount, 15)

    def test_get_age_based_discount_nonexistent_user(self):
        """Test discount for non-existent user"""
        discount = self.manager.get_age_based_discount("nonexistent@example.com")
        self.assertEqual(discount, 0)  # Or appropriate error handling

    def test_get_user_statistics_counts(self):
        """Test correct user counting"""
        stats = self.manager.get_user_statistics()

        # Check if all categories are present
        self.assertIn('child_count', stats)
        self.assertIn('adult_count', stats)
        self.assertIn('senior_count', stats)
        self.assertIn('active_count', stats)
        self.assertIn('total_count', stats)

        # Check sums
        total_calculated = stats['child_count'] + stats['adult_count'] + stats['senior_count']
        self.assertEqual(stats['total_count'], total_calculated)

    def test_get_user_statistics_after_deactivation(self):
        """Test statistics after user deactivation"""
        self.manager.deactivate_user("john@example.com")
        stats = self.manager.get_user_statistics()

        # Should be 3 active users out of 4
        self.assertEqual(stats['active_count'], 3)
        self.assertEqual(stats['total_count'], 4)


if __name__ == '__main__':
    unittest.main()