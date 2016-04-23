from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .message import Message
from .models import User

@csrf_exempt
def index(request):
    
    if request.method == 'POST':
        response = _bot_chat(request.body)
        _process_response(response)
    else:    
        response = _verify_bot(
                               request.GET.get('hub.verify_token'),
                               request.GET.get('hub.challenge')
                    )
            
    return HttpResponse(response)

def _process_response(response):
    if response is not None:
        
        if response.action == 'save_user':
            user = User.objects.get_or_create(fb_id=response.data['id'])
            user.first_name = response.data['first_name']
            user.save()
            
        elif response.action == 'save_location':
            user = User.objects.get(fb_id=response.data['id'])
            user.current_location = response.data['location']
            user.save()
            
        #elif response.action == 'feel_good':
            
        #elif response.action == 'feel_bad':
                    
    return None


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
    
