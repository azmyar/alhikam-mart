from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_item_model_fields(self):
        self.assertTrue(Item.name)
        self.assertTrue(Item.stock)
        self.assertTrue(Item.description)

    def test_context_variable_existence(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.context)
        self.assertIn('name', response.context)
        self.assertIn('class', response.context)

    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')