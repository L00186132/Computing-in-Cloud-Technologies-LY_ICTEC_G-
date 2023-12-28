'''
 Name:           main.py
 Description:    entry point for running application.
 Author:         PJ McMenamin - 14-NOV-2023
 Modified: 
'''
from src.server.udp_server import Server

def main():
    init_server = Server()
    init_server.run("true")


if __name__ == '__main__':
    main()
