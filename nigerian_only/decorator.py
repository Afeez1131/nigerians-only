from functools import wraps

from django.conf import settings
from django.shortcuts import render

from nigerian_only.utils import get_client_ip, is_client_from_whitelisted_countries


def whitelisted_country_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        client_ip = get_client_ip(request)
        WHITELISTED_IPS = getattr(settings, 'WHITELISTED_IPS', [])
        if client_ip not in WHITELISTED_IPS and not is_client_from_whitelisted_countries(client_ip):
            return render(request, '403.html', status=403)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

