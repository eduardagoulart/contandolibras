from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / deve retornar o status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Testa a existência do template"""
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_html(self):
        """Html deve conter as tags de entrada"""
        self.assertContains(self.resp, 'target="_blank"')
        self.assertContains(self.resp, '<iframe', 4)