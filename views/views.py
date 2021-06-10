# Create your views here.
import requests
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render

from views.forms import ViewForm
from views.models import View


def index(request):
    if request.method == 'POST':
        form = ViewForm(request.POST)
        if form.is_valid():
            view = form.save()
            view.user = request.user
            view.save()
    else:
        form = ViewForm()

    views = View.objects.all()
    return render(request, 'views/index.html', {'form': form, 'views': views})


def create_view(request):
    api_url = settings.AZ_CONTENT_MODERATOR_URL
    headers = {'Ocp-Apim-Subscription-Key': settings.AZ_SUBSCRIPTION_KEY,
               'Content-Type': 'text/plain'}
    response = requests.post(api_url,
                             'Is this a crap email abcdef@abcd.com, phone: 6657789887, IP: 255.255.255.255, 1 Microsoft Way, Redmond, WA 98052',
                             headers=headers)
    return JsonResponse(response.json())


def detail(request, pk):
    view = View.objects.get(pk=pk)

    return render(request, 'views/view_detail.html', {'view': view})
