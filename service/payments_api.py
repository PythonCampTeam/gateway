import hug
from integration import payment_rpc
import falcon
#from integration import notification_rpc
#from integration import shipping_rpc
import json


class PaymentAPI(object):
    """Class for created requests and worked with objects Payments"""

    @hug.object.post('/api/cart/add/')
    def add_in_cart(self, **body):
        """Method put product in cart, with quantity
        Args:
            body(dict) body request
        Returns:
            Object of cart if success called
        """
        if body is None:
            return falcon.HTTP_400
        product = payment_rpc.add_in_cart(body)
        return product

    @hug.object.get('/api/cart/')
    def cart(self):
        """Get all products in cart"""
        return payment_rpc.get_cart()

    @hug.object.put('/api/cart/update/')
    def update_cart(self, **body):
        """Update quantity of given product in the cart
        """

        product = payment_rpc.update_cart(body)
        return product

    @hug.object.delete('/api/cart/delete/')
    def delete_item(self, **kwargs):
        product_id = kwargs.get('ID')
        product = payment_rpc.delete_item(product_id)
        return product

    @hug.object.delete('/api/cart/delete_all/')
    def delete_all(self):
        return payment_rpc.delete_cart()

    @hug.object.post('/api/cart/chekout/')
    def checkout(self, **kwargs):
        mail_customer = kwargs.get('mail')
        shipping = kwargs.get('shipping')
        # shipping =
        payment_rpc.new_order(shipping, mail_customer)
        # notification_rpc.send_email(mail_customer)
