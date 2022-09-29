from django.shortcuts import render
from django.http.response import HttpResponse ,JsonResponse

def apage(request):
    return JsonResponse({
                        "Username":"hojjat",
                        "email":"test@test.com",
                        })
