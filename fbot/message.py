import json

class Message:
    
    bot_message = ''
    message = 'Hello'
    user_id = ''
    
    
    def __init__(self, message_json):
        self.bot_message = json.loads(message_json)['entry']
        self.message = self.bot_message['messaging'][0]['message']
                
        #self.message = self.bot_message.message
    
    def reply(self):
        reply = self.process_input()
        return reply;
    
    def process_input(self):
        message = self.message['text'].lower()
        reply = 'Hmmm...'
        if message == 'hello' or message == 'hey':
            reply = 'Hello! How do you feel today?'
            
            
        return reply    