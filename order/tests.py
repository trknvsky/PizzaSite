from django.test import TestCase


class UrlsTest(TestCase):	
    def test_order_page(self):
        response = self.client.get("/order/")
        self.assertEqual(response.status_code, 200)
