from django.test import TestCase, client, override_settings
from nigerian_only.enums import CountryCode

BASE_URL = 'http://127.0.0.1:8000'
REMOTE_ADDR = '98.98.142.106'
NG_REMOTE_ADDR = '102.89.76.223'

# 18.171.135.250 / GB: 98.98.142.106 / 18.133.241.49 / NG: 102.89.76.223


class TestNigerianOnlyMiddleware(TestCase):
    def setUp(self):
        self.client = client.Client()

    def tearDown(self):
        super().tearDown()

    @override_settings(GEOIP_PATH=None)
    def test_middleware_without_geoip_file_path(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR=REMOTE_ADDR)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(WHITELISTED_COUNTRIES=[])
    def test_middleware_without_whitelisted_countries(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR=REMOTE_ADDR)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    def test_middleware_client_ip_in_whitelisted_ips(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR='127.0.0.1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(GEOIP_PATH='incorrect')
    def test_middleware_without_valid_geoip_file_path(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR=REMOTE_ADDR)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")

    @override_settings(WHITELISTED_COUNTRIES=[CountryCode.UG])
    def test_middleware_request_from_non_whitelisted_country(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR=REMOTE_ADDR)
        self.assertEqual(response.status_code, 403)
        self.assertIn("forbidden", str(response.content.lower()))

    @override_settings(WHITELISTED_COUNTRIES=[CountryCode.NG])
    def test_middleware_request_from_whitelisted_countries(self):
        response = self.client.get(BASE_URL, REMOTE_ADDR=NG_REMOTE_ADDR)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the Nigerian Only home page.")



