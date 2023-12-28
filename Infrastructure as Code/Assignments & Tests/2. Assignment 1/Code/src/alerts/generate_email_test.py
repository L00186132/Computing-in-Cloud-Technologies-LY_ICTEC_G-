'''
 Name:           test_generate_email.py
 Description:    class used to test email notification
 Author:         PJ McMenamin - 19-NOV-2023
 Modified:
'''
import unittest
from generate_email import EmailNotification

class test_generate_email(unittest.TestCase):
    ''' test_generate_email() class for testing Email Notification '''

    def test_send_email(self):
        e_note = EmailNotification()
        status = e_note.send_email("Sensor_100","test Data")
        self.assertEqual(status, 1)

if __name__ == '__main__':
    unittest.main()
