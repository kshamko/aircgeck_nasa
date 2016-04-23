import json
import urllib2

class Message:
    
    fb_token = 'EAAX6dRFN4A4BAN4BUe3PWoiSwajNVkDkADu9A2N23yrf8eAAis6djDVFnU6buxLgyw6cPIYB0M2jSPPuYCv3GyuZBZCiRqFt14lSZCmZBllWEzkI2MSs1MX7Mm9KipsI0VfVnOdxyxlAMnSQPWBUOCet8CSByZBXlkB9Q9VGPRQZDZD'
    fb_reply_url = 'https://graph.facebook.com/v2.6/me/messages'
    bot_message = ''
    message = {}
    sender = 0
    
    
    def __init__(self, message_json):
        self.bot_message = json.loads(message_json)['entry'][0]
        self.message = self.bot_message['messaging'][0]['message']
        self.sender = self.bot_message['messaging'][0]['sender']['id']     
        #self.message = self.bot_message.message
    
    def reply(self):
        reply = self.process_input()
        
        data = {
            "recipient": {"id": self.sender},
            "message": {"text": reply},
        }
        
        #json_data = json.dump(data)
        
        fb_msg_url = self.fb_reply_url + '?access_token=' + self.fb_token
        urllib2.urlopen(fb_msg_url, json.dumps(data))
         
        return reply;
    
    def process_input(self):
        message = self.message['text'].lower()
        reply = 'Hmmm...'
        if message == 'hello' or message == 'hey':
            reply = 'Hello! How do you feel today?'
            
            
        return reply    