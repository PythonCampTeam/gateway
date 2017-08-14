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

    @hug.object.get('/api/products/list/{limit}', examples='limit=100')
    def products_list(self, limit: int):
        """Get list of available product"""
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            products = rpc.ProductsRPC.list_products(limit)
        return products

    @hug.object.get('/api/products/{ID}',
                    examples='ID=prod_BBZJ2ka5SKzKn7')
    def products_id(self, **kwargs):
        """Connect to stripe and obtain information about product"""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.getproduct(ID_product)
        return product

    @hug.object.post('/api/products/post/{ID}',
                     examples='ID=prod_BBZJ2ka5SKzKn7')
    def testpost1(self, **kwargs):
        ID_product = kwargs.get('ID')
        return {'id': ID_product}

    @hug.object.delete('/api/products/delete/{ID}',
                       examples='ID=prod_BBs1U1qwftIUs9')
    def product_delete(self, **kwargs):
        """Connect to stripe and delete product"""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.delete_product(ID_product)
        return product

    @hug.object.post('/api/products/create/')
    def products_created(self, body):
        """This example shows how to
        read in post data w/ hug outside of its automatic param parsing"""
        convert = dict(body)
        name = convert.get("name")
        description = convert.get("description")
        attributes = convert.get("attributes")
        package_dimensions = convert.get("package_dimensions")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.create_product(name, description,
                                                     attributes,
                                                     package_dimensions)
        return product

    @hug.object.put('/api/products/update/')
    def product_update(self, body):
        """Update product
        Args:
            body (json) parametrs for create product"""
        kwargs = dict(body)
        ID = kwargs.get("ID")
        KEY = kwargs.get("KEY")
        VALUE = kwargs.get("VALUE")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.update_product(ID, KEY, VALUE)
        return ID, KEY, VALUE, product
