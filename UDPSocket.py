import socket
import config

def udp_send(host, data:str):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host[0], host[1])
    message = f"{data}".encode()
    client_socket.sendto(message, server_address)
    print(f"Sended Message: {message}")