import re
from django.conf import settings
from pathlib import Path
from django.shortcuts import render

from nigerian_only.utils import get_client_ip, is_client_from_whitelisted_countries, get_request_origination


# 18.171.135.250 / 98.98.142.106 / 18.133.241.49
class NigerianOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # if file path does not exist, we process the request as normal
        GEOIP_DB_PATH = getattr(settings, 'GEOIP_PATH', None)
        TEST_IP = getattr(settings, 'ALLOWED_TEST_IPS', [])
        WHITELISTED = getattr(settings, 'WHITELISTED_COUNTRIES', [])
        if not GEOIP_DB_PATH:
            return self.get_response(request)

        if not WHITELISTED:
            return self.get_response(request)
        path = Path(GEOIP_DB_PATH)
        if not path.exists() or not path.is_dir():
            return self.get_response(request)
        client_ip = get_client_ip(request)

        if (not TEST_IP.__contains__(client_ip) and not
        is_client_from_whitelisted_countries(client_ip)):
            return render(request, '403.html', status=403)

        return self.get_response(request)
