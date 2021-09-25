from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''test createing a new user with email is successful'''
        email = 'lnl2048@gmail.com'
        password = 'asdqwe123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'lnl2048@gmail.com'
        user = get_user_model().objects.create_user(email=email, password='asdqwe123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test create_user with no email raise error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password='asdqwe123')

    def test_create_new_superuser(self):

        user = get_user_model().objects.create_superuser('lnl2048@gmail.com', 'sook6836551')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)