from django.test import TestCase
# from application.views import IndexView

class IndexViewTest(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_post_text(self):
        data = {'hayato': "DDD"}
        response = self.client.post('/',data)
        self.assertEqual(response.status_code,200)

