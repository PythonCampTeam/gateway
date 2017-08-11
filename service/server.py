import hug
from service.shipping_api import ShippingAPI
from service.notifications_api import NotificationsAPI

route = hug.route.API(__name__)
route.object('/api/shipping')(ShippingAPI)
route.object('/api/notifications')(NotificationsAPI)
