import unittest
from unittest.mock import MagicMock, patch
import hug
from gateway.service import server as api
from gateway.service.payments_api import PaymentAPI
from gateway.integration import payment_rpc


class TestPayments(unittest.TestCase):
    def setUp(self):
        self.hug_api = api
        self.id1 = 'prod_BDQT7ifqt1FFc1'
        self.id2 = 'prod_BF2pHek9EyzO2S'
        self.id3 = 'prod_BF3PxrZrcpb09X'
        self.body_order = {
            "email": "varvara.malysheva@saritasa.com",
            "phone": "+79994413746",
            "name": "Chloe Taylor",

            "address": {
                "line1": "1092 Indian Summer Ct",
                "city": "San Jose",
                "state": "CA",
                "country": "US",
                "postal_code": "95122"
                    }
            }
        self.body_pay = {"order_id": "or_1AuHBMBqraFdOKT2PQySCVY5",
                         "cart": "tok_mastercard"
                         }

    def test1(self):
        test = hug.test.post(self.hug_api, '/api/cart/add/',
                             params={"product_id": self.id1, "quality": 2})
        print(test.data, test.status, '1')

    def test2(self):
        hug.test.post(self.hug_api, '/api/cart/add/',
                      params={"product_id": self.id1, "quality": 2})
        test = hug.test.put(self.hug_api, '/api/cart/update/',
                            params={"product_id": self.id1, "quality": 1})
        print(test.data, test.status, '2')

    def test3(self):
        test = hug.test.get(self.hug_api, '/api/cart/')
        print(test.data, test.status, '3')

    def test11(self):
        test = hug.test.post(self.hug_api, '/api/cart/chekout/',
                             params={})
        print(test.data, test.status, '4')

    def test4(self):
        hug.test.post(self.hug_api, '/api/cart/add/',
                      params={"product_id": self.id1, "quality": 2})
        test = hug.test.delete(self.hug_api, '/api/cart/delete/',
                               params={"product_id": self.id1})
        print(test.data, test.status, '5')

    def test_mocke_order(self):

        payment_rpc.new_order = MagicMock(return_value='200')
        test = hug.test.post(self.hug_api, '/api/cart/chekout/',
                             params=self.body_order)
        print(test.data, test.status, '6')

    def test_mock_pay(self):
        payment_rpc.order_payd = MagicMock(return_value='200')
        test = hug.test.post(self.hug_api, '/api/cart/paid/',
                             params=self.body_pay)
        print(test.data, test.status, '7')

    def test_mock_select(self):
        payment_rpc.select_shipping = MagicMock(return_value='200')
        test = hug.test.put(self.hug_api, '/api/cart/shipping/',
                            params={"order_id": '11test', "shipping_id": "11test"})
        print(test.data, test.status, '9')

    def test5(self):
        test = hug.test.delete(self.hug_api, '/api/cart/delete_all/')
        print(test.data, test.status, '8')

    def tearDown(self):
        test = hug.test.delete(self.hug_api, '/api/cart/delete_all/')
        print(test.data, test.status, '8')


if __name__ == '__main__':
    unittest.main()
