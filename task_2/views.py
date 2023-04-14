from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def get_token_view(request):
    response = JsonResponse({})
    response['X-CSRFToken'] = get_token(request)
    return response
