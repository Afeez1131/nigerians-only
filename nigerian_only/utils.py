from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2, GeoIP2Exception
from nigerian_only.enums import CountryChoices
from nigerian_only.exceptions import LocalIpException


def is_local_ip(ip):
    local_ips = ['127.0.0.1']
    return ip in local_ips

def get_client_ip(request):
    """
    Get the client's IP address
    :param request:
    :return: ip address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_request_origination(client_ip):
    """
    Get the origination of the request
    :param client_ip:
    :return: request origination (country)
    """
    geo = GeoIP2()
    if is_local_ip(client_ip):
        raise LocalIpException(client_ip)
    try:
        response = geo.country(client_ip)
        country = response.get('country_code', '')
    except GeoIP2Exception:
        return None
    except Exception as e:
        return None
    return country


def is_client_from_whitelisted_countries(client_ip):
    """
    Check if the request is from a country in the WHITELISTED_COUNTRIES list
    :param client_ip:
    :return: boolean
    """
    WHITELISTED = getattr(settings, 'WHITELISTED_COUNTRIES', [CountryChoices.Nigeria])
    country = get_request_origination(client_ip)
    return country in WHITELISTED

