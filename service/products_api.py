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

    @hug.object.get('/api/products', examples='/')
    def test(self):
        """Get list of available product"""
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            products = rpc.ProductsRPC.list_products()
        return products

    @hug.object.get('/api/products/{ID}',
                    examples='ID=prod_BBZJ2ka5SKzKn7')
    def products_id(self, **kwargs):
        """Connect to stripe and obtain information about product"""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.getproduct(ID_product)
        return product

    # @hug.object.post('/api/products/create',
    #                  examples='name=NoteBook&description=Dell')
    # def products_created(self, **kwargs):
    #     """Connect to stripe and obtain information about product"""
    #     name = kwargs.get('n    ame')
    #     description = kwargs.get('description')
    #     attributes = kwargs.get('attributes')
    #     package_dimensions = kwargs.get('package_dimensions')
    #     # ID_product = kwargs.get('ID')
    #     with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
    #         product = rpc.ProductsRPC.getproduct(name=name,
    #                                              description=description,
    #                                              attributes=attributes,
    #                                              package_dimensions=
    #                                              package_dimensions)
    #     return product

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
        # name = body["name"]
        # description = body["description"]
        # attributes = body["attributes"]
        # package_dimensions = body["package_dimensions"]
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.create_product(name, description,
                                                     attributes,
                                                     package_dimensions)
        return product
        # return name, description, attributes, package_dimensions, kwargs

# name = kwargs.get("name")
# description = kwargs.get("description")
# attributes = kwargs.get("attributes")
# package_dimensions = kwargs.get("package_dimensions")
    # @hug.object.get('/api/products/{list}',
    #                 examples='')
    # def list_products(self, **kwargs):
    #     """Return list og products"""
    #     count = kwargs.get('count')
    #     with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
    #         res = rpc.ProductsRPC.list_products()
    #     return res

    # @hug.object.get('/api/products', examples='name=NoteBook&category=Dell')
    # def test(self, name: str):
    #     """testing"""
    #     with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
    #         state = rpc.ProductsRPC.testing(name=name)
    #         state2 = rpc.ProductsRPC.__doc__
    #     return {name: state, '100': state2}
