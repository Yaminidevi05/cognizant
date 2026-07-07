import importlib

django_http = importlib.import_module("django.http")
HttpResponse = django_http.HttpResponse

def hello_view(request):
    return HttpResponse("Course Management API is running")