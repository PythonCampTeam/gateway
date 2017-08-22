import hug
from integration import products_rpc


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
        products = products_rpc.list_products(limit)
        return products


    @hug.object.get('/api/products/{ID}',
                    examples='ID=prod_BBZJ2ka5SKzKn7')
    def products_id(self, **kwargs):
        """Connect to stripe and obtain information about product
        Args:
            ID (string) ID product to return
        Return:
            Returns a product object if the call succeeded."""
        id_product = kwargs.get('ID')
        product = products_rpc.getproduct(id_product)
        return product

    @hug.object.get('/api/products/filter/{category}{order_by}',
                    examples='category=toys&order_by=name')
    def products_filter(self, **kwargs):
        """Product Filtering
        Args:
            category (string) category for search products
            DESC (bool) sorting direction
            order_by (string) parameter for to sorty
        Return:
            Sorted products list."""
        category = kwargs.get('category')
        DESC = False
        order_by = kwargs.get('order_by')
        if order_by[0] == '-':
            DESC = True
            order_by = order_by[1:]
        product = products_rpc.filter_products(category, order_by, DESC)
        return product

    @hug.object.get('/api/products/sorted/{order_by}',
                    examples='order_by=name')
    def products_sorted(self, **kwargs):
        """Returns the sorted product list
        Args:
            order_by (str) parameter for to sorty
        Returns:
            Sorted products list"""
        desc = False
        order_by = kwargs.get('order_by')
        if order_by[0] == '-':
            desc = True
            order_by = order_by[1:]
        product = products_rpc.sorted_products(order_by, desc)
        return product

    @hug.object.get('/api/products/search/{search}{order_by}',
                    examples='search=dogs&order_by=price')
    def products_searched(self, **kwargs):
        """Returns the sorted product list
        Args:
            search (string) parameter for to searching
            order_by (string) parameter for to sorty
            DESC (bool) sorting direction
        Returns:
            Sorted products list"""
        search = kwargs.get('search')
        desc = False
        order_by = kwargs.get('order_by')
        if order_by[0] == '-':
            desc = True
            order_by = order_by[1:]
        product = products_rpc.search_products(search, order_by, desc)
        return product

    @hug.object.delete('/api/products/delete/{ID}',
                       examples='ID=prod_BBs1U1qwftIUs9')
    def product_delete(self, **kwargs):
        """Connect to stripe and delete product
        Args:
            id_product (string) ID product to delete
        Returns:
            Returns an object with a deleted parameter on success.
            Otherwise, this call raises an error."""
        id_product = kwargs.get('ID')
        product = products_rpc.delete_product(id_product)
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
        product = products_rpc.create_product(convert)
        return product

    @hug.object.put('/api/products/update/')
    def product_update(self, body):
        """Updates the product
        Note: Note that a product’s attributes are not editable.
        Args:
            id_product (string) The ID of the product to update.
            key (string) The parameter to update.
            value New value for the parameter
        Returns:
            Returns the product object if the update succeeded."""
        kwargs = dict(body)
        id_product = kwargs.get("id_product")
        key = kwargs.get("key")
        value = kwargs.get("value")
        product = products_rpc.update_product(id_product, key, value)
        return product


@hug.exception(Exception)
def hendl(ex):
    print(ex)
