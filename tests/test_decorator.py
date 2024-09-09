from django.http import HttpResponse, HttpResponseForbidden
from django.test import TestCase

from tests import TestIP
from tests.client import CustomClient

URL = "http://127.0.0.0.1:8000/restricted"
ALL_TEST_IPS = TestIP.ALL_IPS
US_IP = TestIP.IPS['US'][0]
NG_IP = TestIP.IPS['NG'][0]

class TestIsFromNigeria(TestCase):
    def setUp(self):
        self.client = CustomClient()

    def test_restricted_view_with_not_whitelisted_ips_and_not_nigerian(self):
        response = self.client.get(URL, HTTP_X_FORWARDED_FOR=US_IP)
        self.assertEqual(response.status_code, 403)
        self.assertIn("forbidden", str(response.content.lower()))
        self.assertIsInstance(response, HttpResponseForbidden)
        # self.assertTemplateUsed(response, '403.html')

    def test_resticted_page_with_not_whitelisted_ips_from_nigerian(self):
        response = self.client.get(URL, HTTP_X_FORWARDED_FOR=NG_IP)
        self.assertEqual(response.status_code, 200)
        self.assertIn("restricted page", str(response.content))
        self.assertIsInstance(response, HttpResponse)
