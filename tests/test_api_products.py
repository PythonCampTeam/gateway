import hug

try:
    from gateway.service.products_api import ProductsAPI
    from gateway.integration import products_rpc
except ImportError:
    from service.products_api import ProductsAPI
    from integration import products_rpc

from unittest.mock import MagicMock, patch
# import unittest

# class ProductsTest(unittest.TestCase):
hug.test.get(happy_birthday, 'happy_birthday', {'name': 'Timothy', 'age': 25}) # Returns a Response object
