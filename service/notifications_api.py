# import falcon
import hug
import nameko

from gateway.integration import notifications_rpc


class NotificationsAPI(object):

    @hug.object.post('/api/notifications/email/')
    def send_email(self, to_email: hug.types.text,
                   label: hug.types.text,
                   from_email: hug.types.text="test@example.com",
                   subject: hug.types.text = "PythonCamp ZooShop",
                   name: hug.types.text = "Customer",
                   ):
        """This method send an email to customer and notify him.
        Args:
            to_emails (str) : email of customer
            from_emails(str): email of shop
            subject (str): subject of mail
            name (str): name of customer
            label (str): link to label of shipping
        Return:
            state (dict): return starus code of response

        """
        # if to_email is None or label is None:
        #     return {"code": falcon.HTTP_400,
        #             "error":
        #             "Required fields to_email, label"}
        state = notifications_rpc.send_email(to_email, label,
                                             from_email, subject, name)
        return state

    @hug.object.post('/api/notifications/sms/')
    def send_sms(self, number: hug.types.text='+79994413746',
                 content: hug.types.text="Your Order is ready"):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, content
        """
        # if number is None:
        #     return {"code": falcon.HTTP_400,
        #             "error":
        #             "Required fields number"}
        state = notifications_rpc.send_sms(number, content)
        return state

    @hug.exception(nameko.exceptions.RemoteError)
    def handle_exception(exception):
        """Handles the provided exception for testing"""
        return {"messages": "O_o"}
