import json
import urllib2
from .symptoms import Symptoms
from .botresponse import BotResponse

class Message:
    
    fb_token = 'EAAX6dRFN4A4BAN4BUe3PWoiSwajNVkDkADu9A2N23yrf8eAAis6djDVFnU6buxLgyw6cPIYB0M2jSPPuYCv3GyuZBZCiRqFt14lSZCmZBllWEzkI2MSs1MX7Mm9KipsI0VfVnOdxyxlAMnSQPWBUOCet8CSByZBXlkB9Q9VGPRQZDZD'
    fb_reply_url = 'https://graph.facebook.com/v2.6/me/messages' 
    fb_user_url = 'https://graph.facebook.com/v2.6/%s?fields=first_name,last_name,profile_pic&access_token=%s'
    bot_message = ''
    message = {"text": None}
    sender = 0
    user = None
    
    def __init__(self, message_json):
        self.bot_message = json.loads(message_json)['entry'][0]
        
        print message_json
        
        if 'message' in self.bot_message['messaging'][0]:
            self.message = self.bot_message['messaging'][0]['message']
        elif 'postback' in self.bot_message['messaging'][0]:
            self.message['text'] = self.bot_message['messaging'][0]['postback']['payload']
       
       
        self.sender = self.bot_message['messaging'][0]['sender']['id']     
        #self.message = self.bot_message.message
    
    #def reply(self):
    #    reply = self.process_input()
    #    
    #    if reply is not None:
    #        self._send_template_reply('xx')
    #    else:
    #        reply = ''           
    #
    #    return '';
 
    
    def reply(self):
        reply = BotResponse()
                
        fbuser = self._get_fb_user()
        reply.data = {'id': self.sender, 'first_name': fbuser['first_name']}
        
        if self.message['text'] is not None:
            message = self.message['text'].lower()
            
            print '!!!!!!!!user!!!!!!!!!'
            print self.user 
            
            if message == 'hello' or message == 'hey' or message == 'hi':
                text = 'Hello! How do you feel today?'
                buttons = [
                           {"type": "postback", "title": "I'm fine", "payload": "feel_fine_0000"}, 
                           {"type": "postback", "title": "Feeling bad", "payload": "feel_bad_0101"}
                        ]
            
                res = self._send_template_reply(text, buttons)
                reply.action = 'save_user'
                                
            elif message == 'feel_fine_0000':
                res = self._send_text_reply('Great! Nice to hear')
            elif message == 'feel_bad_0101':
                res = self._send_text_reply('Ohhh.. Please tell me your symptoms (comma separated).')       
                reply.action = 'feel_bad'
            elif (self.user is not None): #and self.user and self.user.symptoms_requested:
                reply.action = 'save_symptoms'
                reply.data['symptoms'] = message
                res = self._send_text_reply('Got it. Get well man')  
                
            else:
                self._send_text_reply('Hmmm...')   
                    
        return reply 
    
    def _get_fb_user(self):
        url = self.fb_user_url % (self.sender, self.fb_token)
        request = urllib2.Request(url) 
        response = urllib2.urlopen(request)
        
        #print response.read()
        
        return json.loads(response.read())
        
        
    def _send_template_reply(self, text, buttons):
        
        data = {
             "message":{
                "attachment":{
                   "type":"template",
                   "payload":{
                        "template_type":"button",
                        "text": text,
                        "buttons": buttons
                    }
                }
            }
        }

        return self._send_reply_api(data)
    
    
    def _send_image_reply(self, text, img):
        data = {
            "message": {"text": text},
        }     
        
        return self._send_reply_api(data)
    
    
    def _send_text_reply(self, text):
        data = {
            "message": {"text": text},
        }     
        
        return self._send_reply_api(data)
    
    
    def _send_reply_api(self, data):
        
        data['recipient'] = {"id": self.sender}
        status = False
        fb_msg_url = self.fb_reply_url + '/?access_token=' + self.fb_token
        request = urllib2.Request(fb_msg_url, json.dumps(data), {'Content-Type': 'application/json'})
        
        urllib2.urlopen(request)
          
        return status   
           
    
    
        