import falcon
import hug

from gateway.integration import (
    notifications_rpc,
    payment_rpc,
    shipping_rpc,
    products_rpc,
)


class PaymentAPI(object):
    """Class for created requests and worked with objects Payments
    Args:
        mail_customer(string) email of customer
        phone_customer(string) phone of customer
        order_customer (object) order of customer
        """

    mail_customer = ''
    phone_customer = ''
    order = None

    @hug.object.post('/api/products/ID/buy/')
    def add_in_cart(self, product_id: hug.types.text,
                    quality: int):
        """Method put product in cart, with quantity
        Args:
            body(dict) body request
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

    @hug.object.put('/api/cart/update/')
    def update_cart(self, product_id: hug.types.text,
                    quality: int):
        """Update quantity of given product in the cart

        Args:
            body(dist) parameters for update cart

        Return:
            Updated cart if successful, error message otherwise.

        """
        sku = products_rpc.get_sku_product(product_id)
        product = payment_rpc.update_cart(sku, quality)
        return product

    @hug.object.delete('/api/cart/ID/',
                       examples='product_id=prod_BBs1U1qwftIUs9')
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
        """Delete all products from the cart"""
        return payment_rpc.delete_cart()

    @hug.object.post('/api/cart/chekout/')
    def checkout(self, body):
        """Create a order

        Args:
            body(dist) parameter for order. Contain
            email, phone, name and adress of customer.
            response (dist) result creating order

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
        response = payment_rpc.new_order(body)
        if response.get("error"):
            return response.get("error")
        self.mail_customer = response.get("email")
        self.phone_customer = response.get("phone")
        self.order = response.get("response")
        return self.order, self.mail_customer, self.phone_customer

    @hug.object.put('/api/cart/shipping/')
    def selected_shipping_method(self, order_id, shipping_id):
        """Change shipping method in Order.

        Args:
            body (dict): parameters for update order


        Return:
            order (dict): booking of customer
        """
        self.order = payment_rpc.select_shipping(order_id, shipping_id)
        return self.order

    @hug.object.post('/api/cart/paid/')
    def order_payd(self, order_id, cart="tok_visa"):
        """Change shipping method in Order.

        Args:
            body (dict): parameters for update order.
            Body contain id of order and cart

        Example:
            {
            "cart": "tok_mastercard"
            }

        Return:
            order (dict): booking of customer

        """
        order_paid = payment_rpc.pay_order(order_id, cart)
        if order_paid.get("errors"):
            return order_paid.get("errors")
        shipping_method = order_paid.upstream_id
        label = shipping_rpc.shipment_transaction(
                                                 shipment_id=shipping_method,
                                                 order=order_paid
                                                 )
        data_mail = {"to_email": self.mail_customer,
                     "name": self.customer_name,
                     "label": label,
                     }
        data_sms = {"to_phone": self.phone_customer}
        email = notifications_rpc.send_email(data_mail)
        sms = notifications_rpc.send_sms(data_sms)
        return order_paid, email, sms, label
