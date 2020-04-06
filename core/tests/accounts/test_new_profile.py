from accounts.models import User
from rest_framework.test import APITestCase


class NewProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@mail.com', '123456')

    # Test que prueba que un perfil se crea despues de crear un usuario
    def test_new_article(self):
        auth = self.client.post('/api/token/', {'email': 'test_user@mail.com', 'password': '123456'})
        token = auth.data['access']
        result = self.client.get('/api/v1/profiles/1/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert result.status_code == 200