from django.http import JsonResponse
from .scraping.scraper1 import scrape_data
from django.http import HttpResponse

def textile_data(request):
    data = scrape_data()
    return JsonResponse(data, safe=False)

def home(request):
    return HttpResponse("Welcome to the Textile Website!")