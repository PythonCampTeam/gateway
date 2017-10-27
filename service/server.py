import hug

from gateway.service.notifications_api import NotificationsAPI
from gateway.service.payments_api import PaymentAPI
from gateway.service.products_api import ProductsAPI
from gateway.service.shipping_api import ShippingAPI


@hug.exception(Exception)
def handle_exception(exception):
    print('ERROR')
    return {'error': "Python broke again! Don't blame us! {}".format(
                                                            exception)
            }


@hug.directive()
def session(context_name='session', request=None, **kwargs):
    """Returns the session associated with the current request"""
#    print(context_name, kwargs.get('response').status, ';'*52)
    return request and request.headers or None


route = hug.route.API(__name__)
route.object('/api/shipments')(ShippingAPI)
route.object('/api/products')(ProductsAPI)
route.object('/api/notifications')(NotificationsAPI)
route.object('/api/cart')(PaymentAPI)
