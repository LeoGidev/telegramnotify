import requests

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

    def enviar_mensaje_html(self, mensaje_html):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': mensaje_html,
            'parse_mode': 'HTML'  # Especificar que usamos HTML
        }
        response = requests.post(url, data=data)
        return response.json()

if __name__ == "__main__":
    bot_token = 'REMOVED'  # Reemplaza con tu token
    chat_id = '-4254206027'  # Reemplaza con tu chat_id

    # Crear la tabla en HTML
    mensaje_html = """
    <b>Reporte de Productos</b>
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr>
            <th>Producto</th>
            <th>Ubicación</th>
            <th>Stock</th>
            <th>Mínimo</th>
        </tr>
        <tr>
            <td>Producto A</td>
            <td>Almacén 1</td>
            <td>5</td>
            <td>10</td>
        </tr>
        <tr>
            <td>Producto B</td>
            <td>Almacén 2</td>
            <td>0</td>
            <td>15</td>
        </tr>
        <tr>
            <td>Producto C</td>
            <td>Almacén 3</td>
            <td>8</td>
            <td>8</td>
        </tr>
    </table>
    """

    # Crear el bot e intentar enviar el mensaje
    bot = TelegramBot(bot_token, chat_id)
    respuesta = bot.enviar_mensaje_html(mensaje_html)
    print(respuesta)
