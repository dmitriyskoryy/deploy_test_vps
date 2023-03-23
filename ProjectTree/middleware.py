from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


class Json404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return JsonResponse({"detail": "Not found"}, status=404)
        return response
