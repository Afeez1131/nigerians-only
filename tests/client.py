from django.test import client

class CustomClient(client.Client):
    def __init__(self, *args, **kwargs):
        self.client = client.Client()
        self.default_x_forwarded_for = kwargs.pop('default_x_forwarded_for', None)
        super().__init__(*args, **kwargs)

    def request(self, **request):
        if self.default_x_forwarded_for:
            request.setdefault('HTTP_X_FORWARDED_FOR', self.default_x_forwarded_for)
        return super().request(**request)
