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
        user = CustomUser.objects.get(id=1)
        self.assertEqual(str(user), user.username)
