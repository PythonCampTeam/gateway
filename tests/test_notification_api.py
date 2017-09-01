import unittest

import hug

from gateway.service import server as api


class TestNotiification(unittest.TestCase):
    def setUp(self):
        self.hug_api = api

    def test1(self):
        test = hug.test.post(self.hug_api, '/api/notifications/email/',
                             params={'to_email': 'tamara.malysheva@saritasa.com',
                                     'label': 'bla bla'})
        print(test.data)
        print(test.status)

    def test2(self):
        test = hug.test.post(self.hug_api, '/api/notifications/sms/',
                             params={})
        print(test.data)
        print(test.status)

    def test3(self):
        test = hug.test.post(self.hug_api, '/api/notifications/email/',
                             params={})
        print(test.data)
        print(test.status)

    def test4(self):
        test = hug.test.post(self.hug_api, '/api/notifications/sms/',
                             params={"number": '+79994413741'})
        print(test.data)
        print(test.status)


if __name__ == '__main__':
    unittest.main()


#docker-compose up --build rabbit
#hug -f service/server.py
#nameko run --config config/config.yml rpc.endpoints
