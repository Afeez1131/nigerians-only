from django.http import HttpResponse

from nigerian_only.decorator import is_from_nigeria


def home(request):
    return HttpResponse("Hello, world. You're at the Nigerian Only home page.")


@is_from_nigeria
def restricted_view(request):
    return HttpResponse("Hello, this is a restricted page")
