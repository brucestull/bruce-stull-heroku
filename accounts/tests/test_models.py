from django.test import TestCase

from accounts.models import CustomUser


class CustomUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        CustomUser.objects.create(
            username='DezziKitten',
        )

    def test_dunder_string(self):
        """
        `__str__` method should return the username.
        """
        print("Testing 'CustomUser' __str__ method.")
        user = CustomUser.objects.get(id=1)
        self.assertEqual(str(user), user.username)

class ExampleTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('')
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print('')
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print('')
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_true_is_true(self):
        print('')
        print("Method: test_true_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print('')
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)