import unittest

from src.data_models.User import User

class UserTests(unittest.TestCase):
    
    # Asserts a user is created.
    def test_create_user(self):
        user = User("dummy", "test_password")
        
        self.assertIsInstance(user, User)
        self.assertEqual("dummy", user.user)
        self.assertEqual("test_password", user.password)
        self.assertEqual("user::dummy", user.id)

    # Asserts a ValueError is raised if invalid data is passed to the constructor.
    def test_create_user_invalid_data(self):
        with self.assertRaises(ValueError):
            User("  ", "password")
        
        with self.assertRaises(ValueError):
            User(None, "password")

        with self.assertRaises(ValueError):
            User("user", None)

        with self.assertRaises(ValueError):
            User("user", "    ")

    # Asserts an id can be created.
    def test_create_id(self):
        user = User("dummy", "test_password")
        new_id = user.create_id("new Dummy ")

        self.assertEqual("user::newdummy", new_id)
        self.assertEqual("dummy", user.user)
        self.assertEqual(new_id, user.id)

    # Asserts a ValueError is raised if invalid data is given.
    def test_create_id_invalid_user(self):
        user = User("dummy", "test_password")

        with self.assertRaises(ValueError):
            user.create_id("    ")

        with self.assertRaises(ValueError):
            user.create_id(None)

    # Asserts the __str__() method outputs the correct format.
    def test_str(self):
        user = User("dummy", "test_password")

        self.assertEqual("'id': 'user::dummy' | 'user': 'dummy'", user.__str__())