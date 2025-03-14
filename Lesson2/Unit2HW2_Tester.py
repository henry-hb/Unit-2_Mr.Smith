import unittest
import unittest.mock
from Unit2HW2 import Restaurant,User

class TestRestaurant(unittest.TestCase):
    """Unit testing for Unit2HW2. Make sure you have Unit2HW2.py in the folder as this file
    """

    def setUp(self):
        """Set up a restaurant instance for testing."""
        self.restaurant = Restaurant("Bob's Burgers", "Burgers")

    def test_attributes(self):
        """Test restaurant name and cuisine type attributes."""
        self.assertEqual(self.restaurant.restaurant_name, "Bob's Burgers")
        self.assertEqual(self.restaurant.cuisine_type, "Burgers")
        self.assertEqual(self.restaurant.number_served, 0)

    def test_set_number_served(self):
        """Test describe_restaurant method (output test, requires patching print)."""
        self.restaurant.set_number_served(100)
        self.assertEqual(self.restaurant.number_served,100)

    def increment_number_served(self):
        """Test increment_number_served method."""
        self.restaurant.number_served = 100
        self.restaurant.increment_number_served()
        self.assertEqual(self.restaurant.number_served,101)

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a user instance for testing."""
        self.user = User("Jimmy", "Pesto")
        self.login_attempts = 0

    def test_attributes(self):
        """Test user first and last name attributes."""
        self.assertEqual(self.user.first_name, "Jimmy")
        self.assertEqual(self.user.last_name, "Pesto")
        self.assertEqual(self.login_attempts,0)

    def test_increment_login_attempts(self):
        self.user.login_attempts = 0
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts,1)

    def test_reset_login_attempts(self):
        self.user.login_attempts = 5
        self.user.reset_login_attempts()
        self.assertEqual(self.login_attempts,0)

if __name__ == '__main__':
    unittest.main()