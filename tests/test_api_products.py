import hug
import unittest
from service import server as api
from service.products_api import ProductsAPI
from integration import products_rpc
import stripe
# try:
#     from gateway.service import server as api
#     from gateway.service.products_api import ProductsAPI
#     from gateway.integration import products_rpc
# except ImportError:
#     from service.products_api import ProductsAPI
#     from integration import products_rpc
#     from service import server as api

from unittest.mock import MagicMock, patch
# import unittest


class ProductsAPITest(unittest.TestCase):

    def setUp(self):
        self.hug_api = api
        # self.hug_api = api

    def test_mock_create(self):
        """Test for checking sort product"""
        # obj = ProductsAPI()
        body = {
                "name": "Test"
            }
        products_rpc.create_product = MagicMock(return_value='200')
        print(products_rpc.create_product(body))
        ss = hug.test.post(self.hug_api, '/api/products/', body=body)
        print("create_product sort check")
        print(ss.data, ss.status)
        print("Mock create_product check")

    def test_mock_search_products(self):
        """Test for checking sort product"""
        products_rpc.search_products = MagicMock(return_value='202')
        print(products_rpc.search_products(False, 'name', True))
        ss = hug.test.get(self.hug_api, '/api/products/', category=False,
                          order_by='name', decs=True)
        print("search_products sort check")
        print(ss.data, ss.status)
        print("Mock sorting check")

    def test_get_product(self):
        """Test check methods ProductsAPI.products_id"""
        response1 = hug.test.get(self.hug_api, '/api/products/ID', params={'id_product': 'prod_BBZJ2ka5SKzKn7'})
        print('test_get_product')
        print(response1.status)
        response2 = hug.test.get(self.hug_api, '/api/products/ID', params={})
        print(response2.status)
        response3 = hug.test.get(self.hug_api, '/api/products/ID')
        print(response3.status)

    def test_create_product(self):
        ss = hug.test.post(self.hug_api, '/api/products/', params={})
        print('test_create_product')
        print(ss.status)

    def test_delete_product(self):
        ss = hug.test.delete(self.hug_api, '/api/products/',
                             params={'id_product': 'prod_BBZJ2ka5SKzKn7'})
        print('test_delete_product')
        print(ss.status)
        print(ss)

    def test_update_product(self):
        body = {"name": "TestAPI"}
        ss = hug.test.put(self.hug_api, '/api/products/ID',
                          params={})
        s2 = hug.test.put(self.hug_api, '/api/products/ID',
                          params={'id_product': 'prod_BIMKXrqRkIdC4k'})
        s3 = hug.test.put(self.hug_api, '/api/products/ID',
                          id_product='prod_BIMKXrqRkIdC4k', body=body)
        print('test_update_product')
        print(dir(ss))
        print(ss.status)
        print(s2.status)
        print(s3.status)
        print('/n')
        # print(s2.status)
        # print(s2.headers)
        # print(s2.headers_dict)


if __name__ == '__main__':
    unittest.main()
# hug.test.get(happy_birthday, 'happy_birthday', {'name': 'Timothy', 'age': 25}) # Returns a Response object
