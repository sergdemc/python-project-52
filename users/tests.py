from users.models import User
from django.test import TestCase


class UserCRUDTest(TestCase):

    fixtures = ['users.json']

    def test_create_user(self):
        user_count = User.objects.count()
        User.objects.create(username='test_user', password='test_password')
        self.assertEqual(User.objects.count(), user_count + 1)

    def test_read_user(self):
        user = User.objects.get(username='user1')
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@test.com')

    def test_update_user(self):
        user = User.objects.get(username='user2')
        user.email = 'updated_user2@test.com'
        user.save()
        updated_user = User.objects.get(username='user2')
        self.assertEqual(updated_user.email, 'updated_user2@test.com')

    def test_delete_user(self):
        user_count = User.objects.count()
        User.objects.get(username='user3').delete()
        self.assertEqual(User.objects.count(), user_count - 1)
