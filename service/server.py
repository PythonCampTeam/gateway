import hug
from service.shipping_api import ShippingAPI
from service.products_api import ProductsAPI

route = hug.route.API(__name__)
route.object('/api/shipments')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
