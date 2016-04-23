from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .message import Message
from .models import User
import datetime
 
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
            user.symptoms_requested = False
            user.save()
            
        elif response.action == 'save_location':
            user = User.objects.filter(fb_id=response.data['id'])[0]
            user.current_location = response.data['location']
            user.symptoms_requested = False
            user.save()
            
        elif response.action == 'feel_bad':
            user = User.objects.filter(fb_id=response.data['id'])[0]
            user.symptoms_requested = True
            user.save()
    return None


def _bot_chat(message_json):
   
    bot_msg = Message(message_json)    
    sender = bot_msg.sender;
    bot_msg.user = User.objects.filter(fb_id=sender)[0]
    
    reply = bot_msg.reply()
    
    return reply


def _verify_bot(token, challange):
    response = 'Auth failed! Bad token'
    known_token = 'my_ver_token_05'
    
    if token == known_token :
        response = challange
        
    return response    
    
