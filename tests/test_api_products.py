import hug
import unittest
from gateway.service import server as api
from gateway.integration import products_rpc
# import stripe

from unittest.mock import MagicMock


class ProductsAPITest(unittest.TestCase):

    def setUp(self):
        self.hug_api = api
        self.rpc = products_rpc

    def test_create_product(self):
        """Test for checking api method of created product"""
        body = {
                "name": "Test"
            }
        self.rpc.create_product = MagicMock(return_value='201')
        response_correct = hug.test.post(
                                      self.hug_api,
                                      '/api/products/',
                                      body=body
                                      )
        self.assertEqual(response_correct.data, '201')
        self.assertEqual(response_correct.status, '200 OK')
        self.assertTrue(self.rpc.create_product.called)

        response_handle = hug.test.post(
                                        self.hug_api,
                                        '/api/products/',
                                        params={}
                                        )

        self.assertEqual(response_handle.status, '200 OK')
        self.assertEqual(response_handle.data.get('code'), '400 Bad Request')
        # print("create_product check")
        # print(response_true.data, response_true.status)
        print("Test create product check")

    def test_delete_product(self):
        """Test for checking true delete product"""
        self.rpc.delete_product = MagicMock(return_value='200')
        response_correct = hug.test.delete(
                                           self.hug_api,
                                           '/api/products/ID',
                                           id_product='prod_BIMKqJuS6bHLnX'
                                           )
        self.assertEqual(response_correct.status, '200 OK')
        self.assertEqual(response_correct.data, '200')
        self.assertTrue(self.rpc.delete_product.called)

        response_not_value = hug.test.delete(self.hug_api, '/api/products/ID',
                                             params={})
        self.assertEqual(response_not_value.status, '400 Bad Request')
        self.assertIsNotNone(response_not_value.data.get('errors'))
        print("Test delete product check")
        # print("delete_product check")
        # print(ss.data, ss.status)
        # print("Mock delete_product check")

    def test_search_products(self):
        """Test for checking sort product"""
        self.rpc.search_products = MagicMock(return_value='200')

        response_with_value = hug.test.get(self.hug_api, '/api/products/',
                                           category=False,
                                           order_by='-name')
        self.assertEqual(response_with_value.status, '200 OK')
        self.assertEqual(response_with_value.data, '200')

        response_not_value = hug.test.get(self.hug_api, '/api/products/')
        self.assertEqual(response_not_value.status, '200 OK')
        self.assertEqual(response_not_value.data, '200')
        self.assertTrue(self.rpc.search_products.called)
        # print("search_products sort check")
        # print(response_not_value.data, response_not_value.status)
        # print("Mock sorting check")

    def test_get_product(self):
        """Test check methods api methods get product"""
        self.rpc.get_product = MagicMock(return_value='200')
        response_correct = hug.test.get(
                                        self.hug_api,
                                        '/api/products/ID',
                                        params={'id_product':
                                                'prod_BBZJ2ka5SKzKn7'}
                                        )
        self.assertEqual(response_correct.status, '200 OK')
        self.assertEqual(response_correct.data, '200')
        self.assertTrue(self.rpc.get_product.called)

        # print('test_get_product')
        response_not_value = hug.test.get(self.hug_api, '/api/products/ID')
        self.assertEqual(response_not_value.status, '400 Bad Request')
        self.assertIsNotNone(response_not_value.data.get('errors'))

    def test_update_product(self):
        """Test check methods api methods update product"""
        body = {"name": "TestAPI"}

        self.rpc.update_product = MagicMock(return_value='200')
        response_correct = hug.test.put(
                                        self.hug_api, '/api/products/ID',
                                        id_product='prod_BIMKXrqRkIdC4k',
                                        body=body
                                        )
        self.assertEqual(response_correct.status, '200 OK')
        self.assertEqual(response_correct.data, '200')
        self.assertTrue(self.rpc.update_product.called)

        response_not_value = hug.test.put(self.hug_api, '/api/products/ID')

        self.assertEqual(response_not_value.status, '400 Bad Request')
        self.assertIsNotNone(response_not_value.data.get('errors'))

        response_not_body = hug.test.put(
                                         self.hug_api,
                                         '/api/products/ID',
                                         params={'id_product':
                                                 'prod_BIMKXrqRkIdC4k'}
                                        )
        self.assertEqual(response_not_body.status, '200 OK')
        self.assertEqual(response_not_body.data.get('code'), '400 Bad Request')

        # print('test_update_product')
        # print(ss.status, ss.data)
        # print(s2.status, s2.data)
        # print(s3.status)


if __name__ == '__main__':
    unittest.main()
