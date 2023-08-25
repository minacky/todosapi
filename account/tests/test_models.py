from rest_framework.test import APITestCase
from account.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('minack','nnabuifecyril@gmail.com','kele281985')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'nnabuifecyril@gmail.com')


    def test_creates_super_user(self):
        user = User.objects.create_superuser('minack','nnabuifecyril@gmail.com','kele281985')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'nnabuifecyril@gmail.com')


    def test_raises_error_when_no_username_is_supplied(self):

        self.assertRaises(ValueError,User.objects.create_user,username= '', email='nnabuifecyril@gmail.com',password='kele281985')


    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"The given username must be set"):
            User.objects.create_user(username= '', email='nnabuifecyril@gmail.com',password='kele281985')


    def test_raises_error_when_no_email_is_supplied(self):
        
        self.assertRaises(ValueError,User.objects.create_user,username= "minack", email='', password='kele281985')
        

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"The given email must be set"):
            User.objects.create_user(username= 'minack', email='', password='kele281985')



    def test_raises_error_super_user_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have is_staff=True."):
            User.objects.create_superuser(username= 'minack', email='nnabuifecyril@gmail.com',password='kele281985', is_staff=False)

    def test_is_staff_and_super_user_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have is_superuser=True."):
            User.objects.create_superuser(username= 'minack', email='nnabuifecyril@gmail.com',password='kele281985', is_superuser=False)
        