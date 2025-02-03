import socket
import config
import json

def repack_packet(packet):
    packet = json.loads(packet)
    mess = f"g:{packet["X"]}:{packet["Y"]}:{packet["V"]}:{packet["G"]}:0#"
    return mess



def udp_send(host, data):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host[0], host[1])
    message = f"{data}".encode()
    client_socket.sendto(message, server_address)
    print(f"Sended Message: {message}")


        # # # # # # #g:x:y:v:z;0#


#      {"robot_name":"TrafficLights1_1",
#      "N":"0",
#      "X":200,
#      "Y":0,
#      "T":1,
#      "G":90,
#      "V":0,
#      "L0":"0",
#      "L1":0,
#      "L2":0,
#      "L3":0,
#      "L4":0,
#      "P":"0",
#      "Text":""}


