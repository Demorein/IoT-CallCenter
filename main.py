import threading
import WebSocket
import UDPSocket
import queue
import config

host = config.Man1IP, config.thingport

ws_thread = threading.Thread(target=WebSocket.websocket_thread, daemon=True)
ws_thread.start()

while True:
    try:
        message = WebSocket.message_queue.get(timeout=1)
        print(f"Получено сообщение: {message}")

        message = UDPSocket.repack_packet(message)
        print(f"NOOo {message}")

        UDPSocket.udp_send(host, message)
        

    except queue.Empty:
        pass
