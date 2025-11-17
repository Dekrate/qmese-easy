from datetime import datetime


class UserManager:
    """
    A class to manage users in the system.
    Provides functionality for adding, removing, and querying users.
    """

    def __init__(self):
        """Initialize an empty list of users."""
        self.users = []

    def add_user(self, name, email, birth_date):
        """
        Add a new user to the system.

        Args:
            name (str): The user's full name
            email (str): The user's email address
            birth_date (str): Birth date in "YYYY-MM-DD" format
        """
        user = {
            'name': name,
            'email': email,
            'birth_date': birth_date,
            'registration_date': datetime.now().strftime("%Y-%m-%d"),
            'is_active': True
        }
        self.users.append(user)
        print(f"Added user: {name}")

    def find_user_by_email(self, email):
        """
        Find a user by their email address.

        Args:
            email (str): Email address to search for

        Returns:
            dict: User object if found, None otherwise
        """
        for user in self.users:
            if user['email'] == email:
                return user
        return None

    def deactivate_user(self, email):
        """
        Deactivate a user account.

        Args:
            email (str): Email of the user to deactivate

        Returns:
            bool: True if user was deactivated, False if not found
        """
        user = self.find_user_by_email(email)
        if user:
            user['is_active'] = False
            return True
        return False

    # TODO: Implement the following methods

    def calculate_age(self, birth_date):
        """
        Calculate age based on birth date.

        Args:
            birth_date (str): Birth date in "YYYY-MM-DD" format

        Returns:
            int: Age in years
        """
        # TODO: Implement age calculation
        pass

    def get_age_based_discount(self, email):
        """
        Check if user qualifies for age-based discount:
        - 0-17 years: 20% discount
        - 18-64 years: 0% discount
        - 65+ years: 15% discount

        Args:
            email (str): User's email address

        Returns:
            int: Discount percentage (0, 15, or 20)
        """
        # TODO: Implement discount logic
        pass

    def get_user_statistics(self):
        """
        Generate user statistics.

        Returns:
            dict: Statistics containing:
                - child_count: number of users aged 0-17
                - adult_count: number of users aged 18-64
                - senior_count: number of users aged 65+
                - active_count: number of active users
                - total_count: total number of users
        """
        # TODO: Implement statistics calculation
        pass