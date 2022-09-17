"""Realização de testes do admin com tenants"""
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient


def get_admin_change_view_url(obj: object) -> str:
    return reverse(
        'admin:{}_{}_change'.format(
            obj._meta.app_label,
            type(obj).__name__.lower()
        ),
        args=(obj.pk,)
    )


class BaseSetup(TenantTestCase):

    def setUp(self):
        self.client = TenantClient(self.tenant)
        print(f'Criado tenant: {self.client.tenant}')
        super().setUp()

    def test_user_profile_view(self):
        # criando superuser de testes
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.client.login(username='superuser', password='secret')

        # testando a página principal do Admin
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

        # criar dados de teste e executar
        my_group = Group.objects.create(name='Test Group')
        response = self.client.get(get_admin_change_view_url(my_group))
        self.assertEqual(response.status_code, 200)
