from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.
def test_static(request):
    return render(request, 'test_static.html')
