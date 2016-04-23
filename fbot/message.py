import json

class Message:
    
    bot_message = ''
    message = ''
    user_id = ''
    
    
    def __init__(self, message_json):
        self.bot_message = json.loads(message_json).entry
        self.message = self.bot_message.message
    
    def reply(self):
        reply = self.process_input()
        return reply;
    
    def process_input(self):
        message = message.lower()
        reply = 'Hmmm...'
        if message.text == 'hello' or message.text == 'hey':
            reply = 'Hello! How do you feel today?'
            
            
        return reply    