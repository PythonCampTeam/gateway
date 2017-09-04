import unittest
from unittest.mock import patch

import hug
import stripe

from gateway.service import server as api


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
                         "cart": "tok_mastercard",
                         "upstream_id": "23425"
                         }
        self.body_ship = {"order_id": "or_1AuHBMBqraFdOKT2PQySCVY5",
                          "shipping_id": "tok_mastercard"}
        self.order = stripe.StripeObject().construct_from(
                              self.body_pay, '')

    @patch('gateway.integration.products_rpc.get_sku_product',
           return_value='200')
    @patch('gateway.integration.payment_rpc.add_in_cart',
           return_value='200')
    def test_add_in_cart(self, mock1, mock2):
        print('***********************')
        test = hug.test.post(self.hug_api, '/api/products/ID/buy/',
                             params={"product_id": self.id1, "quality": 2})
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        self.assertTrue(mock2.called)

    def test_add_raise(self):
        print('***********************')
        test = hug.test.post(self.hug_api, '/api/products/ID/buy',
                             params={})
        print(test.status)
        self.assertEqual(test.status, '400 Bad Request')

    @patch('gateway.integration.payment_rpc.get_cart',
           return_value='200')
    def test_cart(self, mock1):
        print('***********************')
        test = hug.test.get(self.hug_api, '/api/cart/')
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)

    @patch('gateway.integration.products_rpc.get_sku_product',
           return_value='200')
    @patch('gateway.integration.payment_rpc.update_cart',
           return_value='200')
    def test_update_cart(self, mock1, mock2):
        print('***********************')
        test = hug.test.put(self.hug_api, '/api/cart/update/',
                            params={"product_id": self.id1, "quality": 2})
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        self.assertTrue(mock2.called)

    def test_update_raise(self):
        print('***********************')
        test = hug.test.put(self.hug_api, '/api/cart/update/')
        self.assertEqual(test.status, '400 Bad Request')
        print(test.status)

    @patch('gateway.integration.products_rpc.get_sku_product',
           return_value='200')
    @patch('gateway.integration.payment_rpc.delete_item',
           return_value='200')
    def test_delete_item(self, mock1, mock2):
        print('***********************')
        test = hug.test.delete(self.hug_api, '/api/cart/ID/',
                               params={"product_id": self.id1})
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        self.assertTrue(mock2.called)
        print(test.status)

    def test_delete_item_raise(self):
        print('***********************')
        test = hug.test.delete(self.hug_api, '/api/cart/ID/')
        self.assertEqual(test.status, '400 Bad Request')
        print(test.status)

    @patch('gateway.integration.payment_rpc.delete_cart',
           return_value='200')
    def test_delete_cart_raise(self, mock1):
        print('***********************')
        test = hug.test.delete(self.hug_api, '/api/cart/')
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        print(test.status)

    @patch('gateway.integration.payment_rpc.new_order',
           return_value={"error": None})
    def test_checkout(self, mock1):
        print('***********************')
        test = hug.test.post(self.hug_api, '/api/cart/chekout/',
                             body=self.body_order)
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        print(test.status)

    @patch('gateway.integration.payment_rpc.select_shipping',
           return_value='200')
    def test_selected_shipping_method(self, mock1):
        print('***********************')
        test = hug.test.put(self.hug_api, '/api/cart/shipping/',
                            body=self.body_ship)
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        print(test.status)

    @patch('gateway.integration.payment_rpc.pay_order')
    @patch('gateway.integration.shipping_rpc.shipment_transaction',
           return_value={"upstream_id": 'id_11111'})
    @patch('gateway.integration.notifications_rpc.send_email',
           return_value='200')
    @patch('gateway.integration.notifications_rpc.send_sms',
           return_value='200')
    def test_order_payd(self, mock1, mock2, mock3, mock4):
        print('***********************')
        mock4.return_value = self.order
        test = hug.test.post(self.hug_api, '/api/cart/paid/',
                             params=self.body_pay)
        self.assertEqual(test.status, '200 OK')
        self.assertTrue(mock1.called)
        self.assertTrue(mock2.called)
        self.assertTrue(mock3.called)
        self.assertTrue(mock3.called)
        print(test.status)


if __name__ == '__main__':
    unittest.main()
