import requests

class TelegramBot:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

    def enviar_mensaje_tabla_simulada(self, mensaje):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': mensaje,
            'parse_mode': 'HTML'  # Usamos HTML solo para estilos básicos
        }
        response = requests.post(url, data=data)
        return response.json()

if __name__ == "__main__":
    # Crear una tabla simulada
    mensaje_simulado = """
<b>Reporte de Productos</b>
<pre>
+------------+------------+--------+--------+
| Producto   | Ubicación  | Stock  | Mínimo |
+------------+------------+--------+--------+
| Producto A | Almacén 1  | 5      | 10     |
| Producto B | Almacén 2  | 0      | 15     |
| Producto C | Almacén 3  | 8      | 8      |
+------------+------------+--------+--------+
</pre>
"""

    # Crear el bot e intentar enviar el mensaje
    bot = TelegramBot()
    respuesta = bot.enviar_mensaje_tabla_simulada(mensaje_simulado)
    print(respuesta)
