import json
import urllib2

class Message:
    
    fb_token = 'EAAX6dRFN4A4BAN4BUe3PWoiSwajNVkDkADu9A2N23yrf8eAAis6djDVFnU6buxLgyw6cPIYB0M2jSPPuYCv3GyuZBZCiRqFt14lSZCmZBllWEzkI2MSs1MX7Mm9KipsI0VfVnOdxyxlAMnSQPWBUOCet8CSByZBXlkB9Q9VGPRQZDZD'
    fb_reply_url = 'https://graph.facebook.com/v2.6/me/messages'
    bot_message = ''
    message = None
    sender = 0
    
    
    def __init__(self, message_json):
        self.bot_message = json.loads(message_json)['entry'][0]
        
        print message_json
        
        if 'message' in self.bot_message['messaging'][0]:
            self.message = self.bot_message['messaging'][0]['message']
       
        self.sender = self.bot_message['messaging'][0]['sender']['id']     
        #self.message = self.bot_message.message
    
    def reply(self):
        reply = self.process_input()
        
        if reply is not None:
            data = {
                "recipient": {"id": self.sender},
                "message": {"text": reply},
            }
            
            fb_msg_url = self.fb_reply_url + '/?access_token=' + self.fb_token
            request = urllib2.Request(fb_msg_url, json.dumps(data), {'Content-Type': 'application/json'})
            try: 
               urllib2.urlopen(request)
            except Exception:
               print 'answer error'
        else:
            reply = ''           
         
        return reply;
    
    def process_input(self):
        reply = None
        if self.message is not None:
            message = self.message['text'].lower()
            reply = 'Hmmm...'
            if message == 'hello' or message == 'hey':
                reply = 'Hello! How do you feel today?'
            
            
        return reply    