from django.http import HttpResponse

from nigerian_only.decorator import whitelisted_country_only


def home(request):
    return HttpResponse("Hello, world. You're at the home page.")


@whitelisted_country_only
def restricted_view(request):
    return HttpResponse("Hello, this is a restricted page")
