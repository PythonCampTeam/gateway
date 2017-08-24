import hug
from service.shipping_api import ShippingAPI
from service.notifications_api import NotificationsAPI


@hug.exception(Exception)
def handle_exception(exception):
    return {'error': "Python broke again! Don't blame us!"}


@hug.directive()
def session(self, context_name='session', request=None, **kwargs):
    """Returns the session associated with the current request"""
    print(context_name, kwargs, '#######'*52)
    return request and request.headers or None


route = hug.route.API(__name__)

route.object('/api/shipping')(ShippingAPI)
route.object('/api/notifications')(NotificationsAPI)
