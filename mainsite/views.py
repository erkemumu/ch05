from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("Hello world!!!")
def about(request,author_no = 0):
    html = "<h1>Here is Author:{}'s about page!</h1><hr>".format(author_no)
    return HttpResponse(html)
def list(request,year,mon,day):
    html = 'Today is {}.{}.{}'.format(year,mon,day)
    return HttpResponse(html)
def company(request):
    return HttpResponse("company")
def sales(request):
    return HttpResponse("sales")
def contact(request):
    return HttpResponse("contact")