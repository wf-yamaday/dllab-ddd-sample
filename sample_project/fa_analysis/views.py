from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # views.py から Application Service を呼び出す
    return HttpResponse("Hello, World")
