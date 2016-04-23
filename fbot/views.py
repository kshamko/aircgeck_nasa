from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import message

@csrf_exempt
def index(request):
    
    if request.method == 'POST':
        
        _bot_chat(request)
        response = 'ok'
    else:    
        response = _verify_bot(
                               request.GET.get('hub.verify_token'),
                               request.GET.get('hub.challenge')
                    )
            
    return HttpResponse(response)



def _bot_chat(request):
    
    message_json = request.POST.body();
    bot_msg = message(message_json)
    reply = bot_msg.reply()
    
    print request



def _verify_bot(token, challange):
    response = 'Auth failed! Bad token'
    known_token = 'my_ver_token_05'
    
    if token == known_token :
        response = challange
        
    return response    
    
