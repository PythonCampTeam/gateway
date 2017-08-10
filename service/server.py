import hug
from service.shipping_api import ShippingAPI

route = hug.route.API(__name__)
route.object('/api/shipping')(ShippingAPI)
