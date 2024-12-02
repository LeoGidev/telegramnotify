import os
from dotenv import load_dotenv
import requests
import xmlrpc.client

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'
        self.verificar()

    def verificar(self):

    
    def enviar_mensaje_telegram(self):
        
        pass

    def send_message(self, message):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message
        }
        response = requests.post(url, data=data)
        return response.json()
    

if __name__ == "__main__":
    load_dotenv()  # Cargar variables desde .env
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = TelegramBot(bot_token, chat_id)

