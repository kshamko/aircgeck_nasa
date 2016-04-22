from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    
    if request.method == 'POST':
        return HttpResponse("ok")
    else:    
        return HttpResponse("You're looking at question")
