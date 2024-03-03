import unittest
from django.test import TestCase, Client
from django.urls import reverse
from main.models import user_data

class UserDataTest(TestCase):
    def setUp(self):
        self.existing_email = 'test1@gmail.com'
        user_data.objects.create(
            login='test1',
            u_password='testp1',
            u_email=self.existing_email,
            press_count=1
        )
        self.client = Client()
    
    def test_existing_email(self):
        response = self.client.post(reverse('signin'), {
            'user-login': 'new_user',
            'user-password': 'new_password',
            'user-email': self.existing_email,
            'user-count': 10
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse(user_data.objects.filter(u_email=self.existing_email, login='new_user').exists())

if __name__ == '__main__':
    unittest.main()