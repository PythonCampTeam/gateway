import falcon
import hug
import cerberus
from gateway.service import validate
from gateway.integration import (notifications_rpc, payment_rpc, products_rpc,
                                 shipping_rpc)

Validator = cerberus.Validator
v = Validator()


class PaymentAPI(object):
    """Class for created requests and worked with objects Payments

    Args:
        mail_customer(string) email of customer
        phone_customer(string) phone of customer
        order_customer (object) order of customer
        customer_name (string) name of customer
        """

    mail_customer = ''
    phone_customer = ''
    order = None
    customer_name = 'Customer'

    @hug.object.post('/api/product/{product_id}/buy/',
                     examples='prod_BBs1U1qwftIUs9')
    def add_in_cart(self, product_id: hug.types.text,
                    quality: hug.types.number):
        """Method put product in cart, with quantity

        Args:
            product_id (string): uniq id of product,
                                 which added in cart.
            quality (int): quantity of product in cart

        Returns:
            Object of cart if success called

        """
        sku = products_rpc.get_sku_product(product_id)
        cart = payment_rpc.add_in_cart(sku, quality)
        return cart

    @hug.object.get('/api/cart/')
    def cart(self):
        """Get all products in cart

        Return:
            Object of cart
        """
        return payment_rpc.get_cart()

    @hug.object.put('/api/cart/{product_id}/',
                    examples='prod_BBs1U1qwftIUs9')
    def update_cart(self, product_id: hug.types.text,
                    quality: hug.types.number):
        """Update quantity of given product in the cart

        Args:
            product_id (string): uniq id of product,
                                 which added in cart.
            quantity (int): quantity of product in cart

        Return:
            Updated cart if successful, error message otherwise.

        """
        sku = products_rpc.get_sku_product(product_id)
        product = payment_rpc.update_cart(sku, quality)
        return product

    @hug.object.delete('/api/cart/{product_id}/',
                       examples='prod_BBs1U1qwftIUs9')
    def delete_item(self, product_id: hug.types.text):
        """Delete product from the cart

        Args:
            product_id (string) id by product to delete

        Return:
            Returns a message aboute delete if the call succeeded.

        """
        sku = products_rpc.get_sku_product(product_id)
        product = payment_rpc.delete_item(sku)
        return product

    @hug.object.delete('/api/cart/')
    def delete_all(self):
        """Delete all products from the cart
        Return:
            Returns a current cart after delete.
        """
        return payment_rpc.delete_cart()

    @hug.object.post('/api/cart/chekout/')
    def checkout(self, body):
        """Create a order

        Args:
            body(dist): Parameters for order. Contain
                       email, phone, name and adress of customer.
            response (dict): Result of creating order.

        Example:
            body = {
                "email": "varvara.malysheva@saritasa.com",
                "phone": "+79994413746",
                "name": "Chloe Taylor",

                "address":{
                    "line1":"1092 Indian Summer Ct",
                    "city":"San Jose",
                    "state":"CA",
                    "country": "US",
                    "postal_code":"95122"
                        }
                }
        Returns:
             Object of order if successful, error message otherwise.

        """
        if body is None or body == {}:
            return falcon.HTTP_400
        if not v.validate(body, validate.schema_order):
            return v.errors
        self.mail_customer = body.get('email')
        self.phone_customer = body.get('phone')
        self.customer_name = body.get('name')
        response = payment_rpc.new_order(body)
        return response

    @hug.object.put('/api/cart/shipping/')
    def selected_shipping_method(self, order_id: hug.types.text,
                                 shipping_id: hug.types.text):
        """Change shipping method in Order.

        Args:
            order_id (string): Uniq id of customer order.
            shipping_id (string): Id of selected shipping.


        Return:
            order (dict): booking of customer
        """
        order = payment_rpc.select_shipping(order_id, shipping_id)
        return order

    @hug.object.post('/api/cart/paid/')
    def order_paid(self, order_id: hug.types.text,
                   card: hug.types.text="tok_visa"):
        """Change shipping method in Order.
        Args:
            order_id (string): Parameters for update order.
            сard (string): Token of card of customet.
        Example:
            {
            "order_id": "or_adahj4344"
            "cart": "tok_mastercard"
            }
        Return:
            order (dict): Booking of customer with status "paid".
        """
        order_paid = payment_rpc.pay_order(order_id, card)
        if order_paid.get("errors"):
            return order_paid.get("errors")
        shipping_method = order_paid.get('upstream_id')
        label = shipping_rpc.shipment_transaction(
            shipment_id=shipping_method,
            order=order_paid,
        )
        notifications_rpc.send_email_with_temp(
            self.mail_customer,
            label,
            self.customer_name,
            order_paid,
        )
        notifications_rpc.send_sms(self.phone_customer)
        return order_paid
