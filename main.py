import os
from dotenv import load_dotenv
import requests
import xmlrpc.client

class TelegramBot:
    def __init__(self, bot_token, chat_id):
