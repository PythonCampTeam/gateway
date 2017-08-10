import hug
<<<<<<< HEAD
from service.gateway import ShippingAPI
from service.gateway import ProductsAPI
=======
from service.shipping_api import ShippingAPI
>>>>>>> develop

route = hug.route.API(__name__)
route.object('/api/shipping')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
