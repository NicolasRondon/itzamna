from accounts.models import User
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@mail.com', '123456')

    def test_auth(self):
        result = self.client.post('/api/token/', {'email': 'test_user@mail.com', 'password': '123456'})
        assert result.status_code == 200
        assert 'access' in result.data

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'email': 'test_user@mail.com', 'password': '123456'})
        token = result.data['access']
        user_result = self.client.get('/api/v1/users/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert user_result.status_code == 200

    def test_str_user(self):
        self.assertEqual(str(self.user), self.user.username)