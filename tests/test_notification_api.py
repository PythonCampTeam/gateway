import unittest
from unittest.mock import patch

from unittest.mock import patch
import hug

from gateway.service import server as api


class TestNotiification(unittest.TestCase):
    """Testing NotificationsAPI"""
    def setUp(self):
        self.hug_api = api

    @patch('gateway.integration.notifications_rpc.send_email',
           return_value='200')
    def test_send_email(self, mock_email):
        """Check that mail sended"""
        test = hug.test.post(self.hug_api, '/api/notifications/email/',
                             params={
                                     'to_email':
                                     'tamara.malysheva@saritasa.com',
                                     'label': 'bla bla'
                                     }
                             )
        print(test.data)
        print(test.status)
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock_email.called)

    @patch('gateway.integration.notifications_rpc.send_sms',
           return_value='200')
    def test_send_sms(self, mock_sms):
        """Check that sms sended"""
        test = hug.test.post(self.hug_api, '/api/notifications/sms/',
                             params={"number": '+79994413741'})
        print(test.data)
        print(test.status)
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock_sms.called)

    def test_mail_raise(self):
        """Check raise if email is empty"""
        test = hug.test.post(self.hug_api, '/api/notifications/email/',
                             params={})
        print(test.data)
        print(test.status)
        self.assertEqual(test.status, '400 Bad Request')

    def test_sms_raise(self):
        """Check raise if number is not valid"""
        test = hug.test.post(self.hug_api, '/api/notifications/sms/',
                             params={"number": '+7999440000'})
        print(test.data)
        print(test.status)


if __name__ == '__main__':
    unittest.main()


# docker-compose up --build rabbit
# hug -f service/server.py
# nameko run --config config/config.yml rpc.endpoints
