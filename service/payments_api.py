import hug
from integration import payment_rpc
import falcon
from integration import notifications_rpc
# from integration import shipping_rpc
# import json


class PaymentAPI(object):
    """Class for created requests and worked with objects Payments
    Args:
        mail_customer(string) email of customer
        phone_customer(string) phone of customer
        order_customer (object) order of customer
        """

    mail_customer = ''
    phone_customer = ''
    order_customer = None

    @hug.object.post('/api/cart/add/')
    def add_in_cart(self, body):
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
        """Get all products in cart

        Return:
            Object of cart
        """
        return payment_rpc.get_cart()

    @hug.object.put('/api/cart/update/')
    def update_cart(self, body):
        """Update quantity of given product in the cart

        Args:
            body(dist) parameters for update cart

        Return:
            Updated cart if successful, error message otherwise.

        """
        product = payment_rpc.update_cart(body)
        return product

    @hug.object.delete('/api/cart/delete/',
                       examples='product_id=prod_BBs1U1qwftIUs9')
    def delete_item(self, product_id):
        """Delete product from the cart

        Args:
            product_id (string) id by product to delete

        Return:
            Returns a message aboute delete if the call succeeded.

        """
        product = payment_rpc.delete_item(product_id)
        return product

    @hug.object.delete('/api/cart/delete_all/')
    def delete_all(self):
        """Delete all products from the cart"""
        return payment_rpc.delete_cart()

    @hug.object.post('/api/cart/chekout/')
    def checkout(self, body):
        """Create a order

        Args:
            body(dist) parameter for order
            response (dist) result creating order

        Returns:
             Object of order if successful, error message otherwise.

        """
        if body is None:
            return falcon.HTTP_400
        response = payment_rpc.new_order(body)
        self.mail_customer = response.get("email")
        self.phone_customer = response.get("phone")
        self.order_customer = response.get("response")
        return self.order_customer, self.mail_customer, self.phone_customer

    @hug.object.put('/api/cart/shipping/')
    def selected_shipping_method(self, body):
        """Change shipping method in Order.

        Args:
            body (dict): parameters for update order

        Return:
            order (dict): booking of customer
        """
        order = payment_rpc.select_shipping(body)
        return order

    @hug.object.put('/api/cart/paid/')
    def order_payd(self, body):
        """Change shipping method in Order.

        Args:
            body (dict): parameters for update order

        Return:
            order (dict): booking of customer
        """
        order = payment_rpc.pay_order(body)
        data_mail = {"to_email": self.mail_customer}
        data_sms = {"to_phone": self.phone_customer}
        res1 = notifications_rpc.send_email(data_mail)
        res2 = notifications_rpc.send_sms(data_sms)
        return order, res1, res2