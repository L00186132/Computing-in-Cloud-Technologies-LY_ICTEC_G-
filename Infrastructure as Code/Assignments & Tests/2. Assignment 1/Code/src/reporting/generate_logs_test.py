'''
 Name:           test_generate_email.py
 Description:    class used to test logging
 Author:         PJ McMenamin - 19-NOV-2023
 Modified:
'''
import unittest
from generate_logs import OutputLog

class test_generate_logs(unittest.TestCase):
    ''' test_generate_logs() class for testing logging functionality '''

    def test_log_creation(self):
        filename = 'test_logfile_'
        extension = '.csv'
        text = 'logs() Class working as expected'

        test_log = OutputLog()
        status = test_log.info_logs(filename, extension, text)
        self.assertEqual(status, 1)



if __name__ == '__main__':
    unittest.main()
