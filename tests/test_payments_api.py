import unittest
import hug
from gateway.service import server as api


class TestPayments(unittest.TestCase):
    def setUp(self):
        self.hug_api = api
        self.id1 = 'prod_BDQT7ifqt1FFc1'
        self.id2 = 'prod_BF2pHek9EyzO2S'
        self.id3 = 'prod_BF3PxrZrcpb09X'

    def test1(self):
        test = hug.test.post(self.hug_api, '/api/cart/add/',
                             params={"product_id": self.id1, "quality": 2})
        print(test.data, test.status)

    def test2(self):
        test = hug.test.put(self.hug_api, '/api/cart/update/',
                            params={"product_id": self.id1, "quality": 1})
        print(test.data, test.status)

    def test3(self):
        test = hug.test.get(self.hug_api, '/api/cart/')
        print(test.data, test.status)

    def test11(self):
        test = hug.test.post(self.hug_api, '/api/cart/chekout/',
                             params={})
        print(test.data, test.status)
        
    def test4(self):
        test = hug.test.delete(self.hug_api, '/api/cart/delete/',
                               params={"product_id": self.id1})
        print(test.data, test.status)

    def test5(self):
        test = hug.test.delete(self.hug_api, '/api/cart/delete_all/')
        print(test.data, test.status)


if __name__ == '__main__':
    unittest.main()
