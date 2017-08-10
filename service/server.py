import hug
from service.gateway import ShippingAPI
from service.gateway import ProductsAPI

route = hug.route.API(__name__)
route.object('/api/shipping')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
