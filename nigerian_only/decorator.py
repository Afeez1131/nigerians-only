from django.conf import settings
from django.shortcuts import render

from nigerian_only.utils import get_client_ip, is_client_from_whitelisted_countries


def is_from_nigeria(view_func):
    def wrapper(request, *args, **kwargs):
        client_ip = get_client_ip(request)
        TEST_IP = getattr(settings, 'WHITELISTED_IPS', [])
        if client_ip not in TEST_IP and not is_client_from_whitelisted_countries(client_ip):
            return render(request, '403.html', status=403)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

