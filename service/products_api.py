import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings


class ProductsAPI(object):
    """Class for created requests and worked with objects Products
        """

    @hug.object.get('/api/products/list/{limit}', examples='limit=100')
    def products_list(self, limit: int):
        """Get list of available product
        Args:
             A limit on the number of objects to be returned.
        Returns:
            Returns a list of products objects if the call succeeded"""
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            products = rpc.ProductsRPC.list_products(limit)
        return products

    @hug.object.get('/api/products/{ID}',
                    examples='ID=prod_BBZJ2ka5SKzKn7')
    def products_id(self, **kwargs):
        """Connect to stripe and obtain information about product
        Args:
            ID (string) ID product to return
        Return:
            Returns a product object if the call succeeded."""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.getproduct(ID_product)
        return product

    @hug.object.post('/api/products/post/{ID}',
                     examples='ID=prod_BBZJ2ka5SKzKn7')
    def testpost1(self, **kwargs):
        """For checking work"""
        ID_product = kwargs.get('ID')
        return {'id': ID_product}

    @hug.object.delete('/api/products/delete/{ID}',
                       examples='ID=prod_BBs1U1qwftIUs9')
    def product_delete(self, **kwargs):
        """Connect to stripe and delete product
        Args:
            ID (string) ID product to delete
        Returns:
            Returns an object with a deleted parameter on success.
            Otherwise, this call raises an error."""
        ID_product = kwargs.get('ID')
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.delete_product(ID_product)
        return product

    @hug.object.post('/api/products/create/')
    def products_created(self, body):
        """Create new product
        Args:
            name (string) The product’s name, for the customer.
            description (string) The product’s description for the customer.
            attributes (lost of strings) A list of up to 5 attributes that each
                                         SKU can provide values for
            package_dimensions (hash) The dimensions of this product for
                                      shipping purposes
            metadata (hash) Set of key/value pairs that you can attach to
                            an object. Use as category
        Returns:
            Returns a product object if the call succeeded.
        """
        convert = dict(body)
        name = convert.get("name")
        description = convert.get("description")
        attributes = convert.get("attributes")
        package_dimensions = convert.get("package_dimensions")
        metadata = convert.get("metadata")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.create_product(name, description,
                                                     attributes,
                                                     package_dimensions,
                                                     metadata)
        return product

    @hug.object.put('/api/products/update/')
    def product_update(self, body):
        """Updates the product
        Note: Note that a product’s attributes are not editable.
        Args:
            ID (string) The ID of the product to update.
            KEY (string) The parameter to update.
            VALUE New value for the parameter
        Returns:
            Returns the product object if the update succeeded."""
        kwargs = dict(body)
        ID = kwargs.get("ID")
        KEY = kwargs.get("KEY")
        VALUE = kwargs.get("VALUE")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            product = rpc.ProductsRPC.update_product(ID, KEY, VALUE)
        return ID, KEY, VALUE, product
