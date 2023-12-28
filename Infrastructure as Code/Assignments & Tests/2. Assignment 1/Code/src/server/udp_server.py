'''
 Name:           udp_server.py
 Description:    listens for packets on a specified network address and port
 Author:         John O'Raw - 13-FEB-2022
 Modified:       PJ McMenamin - 16-NOV-2023
'''
import socket
import config.properties_udp as udp_prop
import config.properties_server as server_prop
import config.properties_temperature as temp_prop
from src.reporting.generate_logs import OutputLog
from src.alerts.generate_email import EmailNotification

class Server():
    ''' server() class is used to listens for packets on a specified address and port '''
    UDP_IP = udp_prop.UDP_PROPERTIES["SERVER_UDP_IPv4"]
    UDP_PORT = udp_prop.UDP_PROPERTIES["SERVER_PORT"]
    BUFFER_SIZE = server_prop.SERVER_PROPERTIES["BUFFER_SIZE"]


    def __init__(self):
        ''' __init__() function to assign values to object properties '''
        print("initialize server() class")
        print(f'UDP server open port at {self.UDP_IP}:{self.UDP_PORT} and being listening')
        print(f'Make sure the actual server IP address matches {self.UDP_IP} in the settings file')


    def logging_enabled(self):
        ''' logging_enabled() checks if logging is enabled '''
        return server_prop.SERVER_PROPERTIES["LOGGING_ENABLED"]


    def alerts_enabled(self):
        ''' alerts_enabled() checks if alerts is enabled '''
        return server_prop.SERVER_PROPERTIES["ALERTS_ENABLED"]


    def get_min_temp(self):
        ''' get_min_temp returns minimum temperature threshold '''
        return temp_prop.TEMPERATURE_PROPERTIES["LOW_TEMP_ALERT"]


    def get_max_temp(self):
        ''' get_max_temp returns maximum temperature threshold '''
        return temp_prop.TEMPERATURE_PROPERTIES["HIGH_TEMP_ALERT"]


    def run(self, parameter1) -> None:
        ''' run() function opens sockets to listen for client data '''
        if self.logging_enabled():
            init_log = OutputLog()

        if self.alerts_enabled():
            init_email = EmailNotification()

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.bind( (self.UDP_IP, self.UDP_PORT) )
            print('Listening on', self.UDP_IP)

            while parameter1:
                data, addr = s.recvfrom(self.BUFFER_SIZE)
                data = data.decode()

                # validate data received
                if len(data) == 0:
                    print('No Sensor data received...')
                elif len(data.split(", ")) == 3:
                    print('Sensor data received...')
                    list_results = data.split(", ")

                    # Logs data retrieved
                    if self.logging_enabled():
                        l_status = init_log.info_logs(list_results[0], '.csv', data)

                        #if l_status == 1:
                        #    print("logs generated successfully")
                        #else:
                        #    print("logs generation error")

                    # retrieve temperature data, checks temperature threshold & sned notification
                    if self.alerts_enabled():
                        temp = int( list_results[1][:-1] )

                        if temp < self.get_min_temp() or temp > self.get_max_temp():
                            # pass info for subject line & email body
                            e_status = init_email.send_email(list_results[0], data)
                            
                            if e_status == 1:
                                print("email notification sent")
                            else:
                                print("email generation error")
                else:
                    print('Invalid Sensor data received... Data skipped')
