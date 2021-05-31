# Create your views here.
import requests
from django.conf import settings

from django.http.response import JsonResponse


def create_view(request):
    api_url = settings.AZ_CONTENT_MODERATOR_URL
    headers = {'Ocp-Apim-Subscription-Key': settings.AZ_SUBSCRIPTION_KEY,
               'Content-Type': 'text/plain'}
    response = requests.post(api_url,
                             'Is this a crap email abcdef@abcd.com, phone: 6657789887, IP: 255.255.255.255, 1 Microsoft Way, Redmond, WA 98052',
                             headers=headers)
    return JsonResponse(response.json())
