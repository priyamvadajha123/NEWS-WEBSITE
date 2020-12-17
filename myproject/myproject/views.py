from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1 style='color:red'>Hello Welcome to my home</h1>")