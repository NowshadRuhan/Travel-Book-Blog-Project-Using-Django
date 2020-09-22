from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

def IndexView(request):
    return HttpResponseRedirect(reverse('App_Blog:blogList'))
