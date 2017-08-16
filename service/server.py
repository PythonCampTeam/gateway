import hug
from service.shipping_api import ShippingAPI
from service.products_api import ProductsAPI
from service.notifications_api import NotificationsAPI

route = hug.route.API(__name__)
route.object('/api/shipments')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
route.object('/api/notifications')(NotificationsAPI)
