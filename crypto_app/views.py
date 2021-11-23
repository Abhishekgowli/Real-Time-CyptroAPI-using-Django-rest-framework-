from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func,crawl_currency
# Create your vie;ws here.
def home(request):
    #test_func.delay()
    crawl_currency()
    return HttpResponse("Hello roject is running ")