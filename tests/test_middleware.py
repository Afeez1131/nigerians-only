import random

from django.test import TestCase, client, override_settings
from nigerian_only.enums import CountryChoices
from tests.client import CustomClient
from . import TestIP

BASE_URL = 'http://127.0.0.1:8000'

ALL_TEST_IPS = TestIP.ALL_IPS
US_IP = TestIP.IPS['US'][0]
NG_IP = TestIP.IPS['NG'][0]

class TestNigerianOnlyMiddleware(TestCase):
    def setUp(self):
        self.client = CustomClient()
        self.random_ip = random.choice(ALL_TEST_IPS)

    @override_settings(GEOIP_PATH=None)
    def test_middleware_without_geoip_file_path(self):
        for ip in ALL_TEST_IPS:
            response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=ip)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(WHITELISTED_COUNTRIES=[])
    def test_middleware_without_whitelisted_countries(self):
        for ip in ALL_TEST_IPS:
            response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=ip)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(WHITELISTED_IPS=[US_IP])
    def test_middleware_client_ip_in_whitelisted_ips(self):
        response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=US_IP)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(GEOIP_PATH='incorrect')
    def test_middleware_without_valid_geoip_file_path(self):
        response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=US_IP)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(WHITELISTED_COUNTRIES=[CountryChoices.Zimbabwe])
    def test_middleware_request_from_non_whitelisted_country(self):
        response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=US_IP)
        self.assertEqual(response.status_code, 403)
        self.assertIn("forbidden", str(response.content.lower()))

    @override_settings(WHITELISTED_COUNTRIES=[CountryChoices.Nigeria])
    def test_middleware_request_from_whitelisted_countries(self):
        response = self.client.get(BASE_URL, HTTP_X_FORWARDED_FOR=NG_IP)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")





