import hug

from gateway.service.notifications_api import NotificationsAPI

from gateway.service.payments_api import PaymentAPI
from gateway.service.products_api import ProductsAPI
from gateway.service.shipping_api import ShippingAPI


route = hug.route.API(__name__)
route.object('/api/shipments')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
route.object('/api/notifications')(NotificationsAPI)
route.object('/api/cart')(PaymentAPI)
