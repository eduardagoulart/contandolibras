from django.test import TestCase

from coala.core.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contato')

    def test_get(self):
        """Pega a pagina /contato e retorna status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Testa a existência do template"""
        self.assertTemplateUsed(self.resp, 'core/contato.html')

    def test_html(self):
        """Html deve conter as tags de entrada"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Formulario contem csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Contexto deve ter o formulario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Formulario deve ter os campos"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'email', 'telefone', 'message'], list(form.fields))
