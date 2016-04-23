from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .message import Message

@csrf_exempt
def index(request):
    
    if request.method == 'POST':
        response = _bot_chat(request.body)
    else:    
        response = _verify_bot(
                               request.GET.get('hub.verify_token'),
                               request.GET.get('hub.challenge')
                    )
            
    return HttpResponse(response)



def _bot_chat(message_json):
   
    bot_msg = Message(message_json)
    reply = bot_msg.reply()
    
    return reply



def _verify_bot(token, challange):
    response = 'Auth failed! Bad token'
    known_token = 'my_ver_token_05'
    
    if token == known_token :
        response = challange
        
    return response    
    
