import json
from http import HTTPStatus

import hug
from nameko.standalone.rpc import ClusterRpcProxy

from gateway.config.settings.common import security as security_settings
from gateway.integration import shipping_rpc


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

    @hug.object.post('/api/shipments')
    def shipments_callback(self, **kwargs):
        """ method work with stripe service when create order
        and answer rates of shipment
        Kwargs(dict): data item of order
        Return:
            dict: with order data updated rates and create shipments
        """

        order_update = shipping_rpc.shipping_order_update(**kwargs)
        return order_update

    @hug.object.get('/api/shipments')
    def shipments_list(self, **kwargs):
        """function return lists of shipments"""
        sort = kwargs.get('order_by')
        print(sort, '#'*25)
        return json.loads(shipping_rpc.shipping_get(order_by=sort))

    @hug.object.get('/api/shipments/{ID}/rates/{CURRENCY}',
                    example='id=cart&currency=USD')
    def shipments_rates(self, session: hug.directives.session, **kwargs):
        """ function return rate for the shipment"""
        shipments_id = kwargs.get('ID')
        shipments_currency = kwargs.get('CURRENCY')

        rates_result = shipping_rpc.shipping_get_rates(
                                    object_id=shipments_id,
                                    object_rates=shipments_currency)

        if rates_result:
            rates_result = json.loads(rates_result)
            print(rates_result.items(), '###'*25)
            if all(rates_result.values()):
                return rates_result
        # raise Exception(session)
        # return rates_result

    @hug.object.post('/api/order')
    def stripe_callback(self, **kwargs):

        return {}

    @hug.object.get('/api/shipments/{ID}/label', example='id=cart_id')
    def shipments_label(self, **kwargs):
        """function generate shipping label"""
        return {}
