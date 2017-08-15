import json
import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings
from integration import shipping_rpc


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
    def shipments_add(self, **kwargs):
        new_shipments = json.dumps(kwargs.get('address_to'))

        return shipping_rpc.shipping_add(address_to=new_shipments)

    @hug.object.get('/api/shipments')
    def shipments_list(self):
        """function return lists of shipments"""
        return shipping_rpc.shipping_get()

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

