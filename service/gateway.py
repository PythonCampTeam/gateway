import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common.security import AMQP_CONFIG


class ShippingAPI(object):
    """ Class for make request on service products
    Args:
        AMQP_CONFIG(dict): dict object from settings file for connect
                            to rabbitmq
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/shipping', examples='name=NoteBook&category=Dell')
    def shipping(self, name: str):
        with ClusterRpcProxy(AMQP_CONFIG) as rpc:
            state = rpc.ShippingRPC.service_state(name=name)
            state2 = rpc.ShipingRPC.__doc__
        return {name: state, '42': state2}


class ProductsAPI(object):
    """ Class for make request on service products
    Args:
        AMQP_CONFIG(dict): dict object from settings file for connect
                            to rabbitmq
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/products', examples='name=NoteBook&category=Dell')
    def products(self, name: str):
        with ClusterRpcProxy(AMQP_CONFIG) as rpc:
            state = rpc.ProductsRPC.getproduct(name=name)
            state2 = rpc.ProductsRPC.__doc__
        return {name: state, '100': state2}
