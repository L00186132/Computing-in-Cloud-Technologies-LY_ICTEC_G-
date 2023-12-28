#######################################################################################
# Name:           udp_client2.py
# Description:    Send UDP packets to a particular address and port.
# Author:         John O'Raw - 13-FEB-2022
# Modified:       PJ McMenamin - 14-NOV-2023
#######################################################################################

import socket
import time
from datetime import datetime
import config.properties_udp as settings
from random import randint

UDP_IP = settings.UDP_PROPERTIES["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP_PROPERTIES["SERVER_PORT"]

print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message_text = f"Raspberry_2, {randint(-20, 45):4}c,  {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (UDP_IP, UDP_PORT))
        print(f'Sent {message_text}')
        time.sleep(5) # real application increast time