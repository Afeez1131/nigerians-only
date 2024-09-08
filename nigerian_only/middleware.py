import re
from django.conf import settings
from pathlib import Path

from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

from nigerian_only.utils import get_client_ip, is_client_from_whitelisted_countries


class NigerianOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        GEOIP_DB_PATH = getattr(settings, 'GEOIP_PATH', None)
        WHITELISTED_IPS = getattr(settings, 'WHITELISTED_IPS', [])
        WHITELISTED_COUNTRIES = getattr(settings, 'WHITELISTED_COUNTRIES', [])
        if not GEOIP_DB_PATH:
            return self.get_response(request)

        if not WHITELISTED_COUNTRIES:
            return self.get_response(request)
        path = Path(GEOIP_DB_PATH)
        if not path.exists() or not path.is_dir():
            return self.get_response(request)
        client_ip = get_client_ip(request)
        if client_ip not in WHITELISTED_IPS and not is_client_from_whitelisted_countries(client_ip):
            raise PermissionDenied

        return self.get_response(request)
