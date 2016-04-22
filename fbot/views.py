from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    
    if request.method == 'POST':
        return HttpResponse("ok")
    else:    
        
        response = 'Alarma!!!'
        
        if request.GET['verify_token'] == 'my_ver_token_05':
            response = request.GET['challenge']
            
        return HttpResponse(response)
