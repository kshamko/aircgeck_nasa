from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .message import Message
from .models import User, Symptom
import datetime
import string
 
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
            (user, ex) = User.objects.get_or_create(fb_id=response.data['id'])#get_or_create(fb_id=response.data['id'])
            user.first_name = response.data['first_name']
            user.symptoms_requested = False
            user.current_location = 'New York'
            user.current_lon = 74.0059
            user.current_lat = 40.7128
            user.save()
           
        elif response.action == 'feel_bad':
            user = User.objects.get(fb_id=response.data['id'])
            user.symptoms_requested = True
            user.save()
            
        elif response.action == 'save_symptoms':
            oUser = User.objects.get(fb_id=response.data['id'])
            symptoms = response.data['symptoms']             
            symptoms = symptoms.split(',')
            
            #user = models.ForeignKey(User, on_delete=models.CASCADE)
            #symption = models.CharField(max_length=200)
            #current_lon = models.FloatField(default=0.0)
            #current_lon = models.FloatField(default=0.0)
            
            for s in symptoms:
                oS = Symptom(user=oUser, symptom=s, current_lon=oUser.current_lon, current_lat=oUser.current_lat)
                oS.save()
            
    return None


def _bot_chat(message_json):
   
    bot_msg = Message(message_json)    
    sender = bot_msg.sender;
    bot_msg.user = User.objects.filter(fb_id=sender)
    
    reply = bot_msg.reply()
    
    return reply


def _verify_bot(token, challange):
    response = 'Auth failed! Bad token'
    known_token = 'my_ver_token_05'
    
    if token == known_token :
        response = challange
        
    return response    
    
