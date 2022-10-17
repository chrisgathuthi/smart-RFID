from django.test import TestCase
from generator.models import Staff,User

# Create your tests here.
class TestStaff(TestCase):
    def test_model_str(self):
        name = Staff.objects.create(name="chris")
        country = Staff.objects.create(country="kenya")
        self.assertEqual(str(name),"chris")
    def test_postlike_users(self):
        testuser = User.objects.create_user(username="chris",password="password")
        testuser2 = User.objects.create_user(username="cathie",password="password")
        obj = Staff.objects.create(name="chris",country="kenya")
        obj.likes.set([testuser.pk,testuser2.pk])
        self.assertEqual(obj.likes.count(),2)


