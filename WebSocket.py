import websocket
import queue
import config

message_queue = queue.Queue()


def on_message(ws, message):
    message_queue.put(message) 


def on_error(ws, error):
    print(f"Ошибка: {error}")


def on_close(ws, close_status_code, close_msg):
    print("WebSocket закрыт")


def on_open(ws):
    print("WebSocket подключен")


def websocket_thread():
    ws = websocket.WebSocketApp(f"ws://{config.serverip}:{config.websport}",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    print(f"ws://{config.serverip}:{config.websport}")
    ws.on_open = on_open
    ws.run_forever()