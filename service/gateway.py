import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings


class ShippingAPI(object):
    """ Class for make request on service products
    Args:
        AMQP_CONFIG(dict): dict object from settings file for connect
                            to rabbitmq
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/products',
                    examples='name=NoteBook&category=Dell')
    def shipments(self, name: str):
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.ShippingRPC.service_state(name=name)
            state2 = rpc.ShipingRPC.__doc__
        return {name: state, '42': state2}



    @hug.object.post('/api/shipments/{ID}',
                     examples='id=shipments_id&shipments=DHL')
    def shipments_add(self, **kwargs):
        new_shipments = kwargs.get('ID')
        return {'id': new_shipments}

    @hug.object.get('/api/shipments')
    def shipments_list(self):
        """function return lists of shipments"""
        return {}

    @hug.object.get('/api/shipments/{ID}/currency/{CURRENCY}',
                    example='id=cart&currency=USD')
    def shipments_rates(self, **kwargs):
        """ function return rate for the shipment"""
        return {}

    @hug.object.get('/api/shipments/{ID}/label', example='id=cart_id')
    def shipments_label(self, **kwargs):
        """function generate shipping label"""
        return {}

