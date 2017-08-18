import hug
from integration import payment_rpc
#from integration import notification_rpc
import json


class PaymentAPI(object):
    """Class for created requests and worked with objects Payments"""

    @hug.object.post('api/cart/add')
    def add_in_cart(self, **kwargs):
        product_id = kwargs.get('ID')
        product = payment_rpc.add_in_cart(product_id)
        return json.dumps(product)

    @hug.object.get('api/cart')
    def cart(self):
        return json.dumps(payment_rpc.get_cart())

    @hug.object.put('api/cart/update')
    def update_cart(self, **kwargs):
        product_id = kwargs.get('ID')
        product = payment_rpc.update_cart(product_id)
        return json.dumps(product)

    @hug.object.delete('api/cart/delete')
    def delete_item(self, **kwargs):
        product_id = kwargs.get('ID')
        product = payment_rpc.delete_item(product_id)
        return json.dumps(product)

    @hug.object.delete('api/cart/delete_all')
    def delete_all(self):
        return payment_rpc.delete_cart()

    @hug.object.post('api/cart/chekout')
    def checkout(self, **kwargs):
        mail_customer = kwargs.get('mail')
        shipping = kwargs.get('shipping')
        payment_rpc.new_order(shipping, mail_customer)
        #notification_rpc.send_email(mail_customer)
