import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings


class ProductsAPI(object):
    """ Hello padla! Class for make request on service products
    Args:
        AMQP_CONFIG(dict): dict object from settings file for connect
                            to rabbitmq
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/products', examples='name=NoteBook&category=Dell')
    def test(self, name: str):
        """testing"""
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.ProductsRPC.testing(name=name)
            state2 = rpc.ProductsRPC.__doc__
        return {name: state, '100': state2}

    @hug.object.get('/api/products/{ID}',
                    examples='ID=prod_BBZJ2ka5SKzKn7')
    def products_id(self, **kwargs):
        """Connect to stripe and obtain information about product"""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            pr = rpc.ProductsRPC.getproduct(ID_product)
        return {ID_product: pr}
