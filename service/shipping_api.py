import json
import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings

from integration import shipping_rpc


@hug.directive()
def session(self, context_name='session', request=None, **kwargs):
    """Returns the session associated with the current request"""
    return request and request.headers or None


class ShippingAPI(object):
    """ Class for make request on service products
    Args:
        AMQP_CONFIG(dict): dict object from settings file for connect
                            to rabbitmq
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """
    @hug.object.get('/api/shipments/state')
    def ship(self, **kwargs):

        return json.loads(shipping_rpc.service_state(name=kwargs))

    @hug.object.post('/api/shipments',
                     examples='id=shipments_id&shipments=DHL')
    def shipments_add(self, body=None, **kwargs):
        new_shipments = json.dumps(kwargs.get('address_to'))
        print(body, 'sesssion')
        print(new_shipments)

        return shipping_rpc.shipping_add(address_to=new_shipments,
                                         session=''
                                         )

    @hug.object.get('/api/shipments{sort}')
    def shipments_list(self, **kwargs):
        """function return lists of shipments"""
        sort = kwargs.get('sort')
        print(sort)
        return shipping_rpc.shipping_get(sort=sort)

    @hug.object.get('/api/shipments/{ID}/currency/{CURRENCY}',
                    example='id=cart&currency=USD')
    def shipments_rates(self, **kwargs):
        sh_id = kwargs.get('ID')
        sh_currency = kwargs.get('CURRENCY')
        """ function return rate for the shipment"""
        return {'id': sh_id, 'sh_currency': sh_currency}

    @hug.object.get('/api/shipments/{ID}/label', example='id=cart_id')
    def shipments_label(self, **kwargs):
        """function generate shipping label"""
        return {}

