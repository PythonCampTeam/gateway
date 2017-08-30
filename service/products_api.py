import falcon
import hug

from gateway.integration import products_rpc


class ProductsAPI(object):
    """Class for created objects Products and worked with them """

    @hug.object.get('/api/products/ID',
                    examples='id_product=prod_BBZJ2ka5SKzKn7')
    def products_id(self, id_product):
        """Connect to stripe and obtain information about product

        Args:
            id_product (string) id by product

        Return:
            Returns a product object if the call succeeded.

        """
        product = products_rpc.get_product(id_product)
        return product

    @hug.object.get('/api/products/',
                    examples='category=toys&order_by=name')
    def products_filter(self, category=False, order_by="name"):
        """Product Filtering

        Args:
            category (string) category for search products
            decs (bool) sorting direction
            order_by (string) parameter for to sorty

        Return:
            Sorted products list.

        """
        decs = False
        if order_by.startswith("-", 0, 1):
            decs = True
            order_by = order_by[1:]
        product = products_rpc.search_products(category, order_by, decs)
        return product

    @hug.object.delete('/api/products/ID',
                       examples='id_product=prod_BBs1U1qwftIUs9')
    def product_delete(self, id_product):
        """Connect to stripe and delete product

        Args:
            id_product (string) ID product to delete

        Returns:
            Returns an object with a deleted parameter on success.
            Otherwise, this call raises an error.

        """
        product = products_rpc.delete_product(id_product)
        return product

    @hug.object.post('/api/products/')
    def products_created(self, body=None):
        """
            Create new product
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
        if body is None:
            return {
                    "code": falcon.HTTP_400,
                    "message": "Fill in the attributes",
                    "attributes": """name, description, attributes,
                    package_dimensions, metadata, inventory"""
                    }
        product = products_rpc.create_product(body)
        return product

    @hug.object.put('/api/products/ID')
    def product_update(self, id_product, body=None):
        """Updates the product

        Args:
            body: (dict) The parameter to update.

        Returns:
            Returns the product object if the update succeeded.

        """
        if body is None or body == {}:
            return {
                    "code": falcon.HTTP_400,
                    "message": "Fill in the attributes"
                    }
        product = products_rpc.update_product(id_product, body)
        return product
