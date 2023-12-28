'''
 Name:           generate_logs.py
 Description:    initiate logging on application.
 Author:         PJ McMenamin - 15-NOV-2023
 Modified:
'''
import sys
import logging
import os
from datetime import datetime as dt

class OutputLog():
    ''' output_logs() class is used to initiate logging on application '''

    def __init__(self):
        ''' __init__() function to assign values to object properties '''
        print("Initializing Logging Class")


    def get_logfile_path(self):
        ''' get_logfile_path() function retrieves logfile path '''

        # CODE REFERENCE: code snipits was taken from John O'Raw - AUT - IaC - Python Lecture notes
        path = ''

        # Checks which OS code is running on
        if sys.platform == 'win32':
            path = "./logfiles/"
        elif sys.platform == 'linux':
            path = '/home/pi/logfiles/'
        else:
            print(f'Unsupported OS: {sys.platform}')
            exit(0)

        # Check if path exists & create logfiles directory if it doesn't exist
        if not os.path.exists(path):
            os.makedirs(path)
            print("New Logfile directory created!")

        return path


    def get_date_extension(self, filename: str, extension: str):
        ''' get_date_extension() function generate Logfile Name'''
        now = dt.now()
        file = filename + '_%0.4d_%0.2d_%0.2d' % (now.year, now.month, now.day) + extension

        return file


    def info_logs(self, filename: str, extension: str, results: str):
        ''' info_logs() function records Log file results '''
        
        try:
            file_path = self.get_logfile_path()
            file_ext = self.get_date_extension(filename,extension)
            path = file_path + file_ext
            #print(path)

            # CODE REFERENCE: following code snipits was taken from stackoverflow.com
            #  - https://stackoverflow.com/questions/41764941/

            # assigns logger configurations and sets Logging Level
            init_logger = logging.getLogger()
            init_logger.setLevel(logging.INFO)

            # configure FileHandler to write to logs and sets Logging Level
            init_filehandler = logging.FileHandler(path)
            init_filehandler.setLevel(logging.INFO)

            # Adds filehandler to logger, write out data & closes filehandler again
            init_logger.addHandler(init_filehandler)
            init_logger.info(results)
            init_logger.removeHandler(init_filehandler)
            return 1
        except Exception as str_error:
            return 0
