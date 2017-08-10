import hug
from service.gateway import ShippingAPI

route = hug.route.API(__name__)
route.object('/api/shipping')(ShippingAPI)
