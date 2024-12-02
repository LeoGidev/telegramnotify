import os
import requests
from dotenv import load_dotenv

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

    def send_message(self, message, parse_mode="Markdown"):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': parse_mode  # Usar Markdown o HTML
        }
        response = requests.post(url, data=data)
        print(response.json())
        return response.json()

    def enviar_tabla(self):
        # Ejemplo de datos
        productos = [
            {"Producto": "Producto A", "Stock": 5, "Mínimo": 10, "Ubicación": "Almacén 1"},
            {"Producto": "Producto B", "Stock": 15, "Mínimo": 10, "Ubicación": "Almacén 2"},
            {"Producto": "Producto C", "Stock": 0, "Mínimo": 5, "Ubicación": "Almacén 3"},
        ]

        # Crear el mensaje con formato Markdown
        mensaje = "*Reporte de Productos*\n\n"
        mensaje += "`{:<20} {:<10} {:<10} {:<15}`\n".format("Producto", "Stock", "Mínimo", "Ubicación")
        mensaje += "`{:<20} {:<10} {:<10} {:<15}`\n".format("-" * 20, "-" * 10, "-" * 10, "-" * 15)

        for producto in productos:
            mensaje += "`{:<20} {:<10} {:<10} {:<15}`\n".format(
                producto["Producto"], producto["Stock"], producto["Mínimo"], producto["Ubicación"]
            )

        # Enviar el mensaje
        self.send_message(mensaje, parse_mode="Markdown")

if __name__ == "__main__":
    # Cargar claves desde .env
    load_dotenv()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    # Inicializar y enviar mensaje
    bot = TelegramBot(bot_token, chat_id)
    bot.enviar_tabla()


