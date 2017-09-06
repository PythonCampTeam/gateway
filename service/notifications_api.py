import hug

from gateway.integration import notifications_rpc


class NotificationsAPI(object):
    """Class for sended notifications for Customer"""

    @hug.object.post('/api/notifications/email/')
    def send_email(
                 self,
                 to_email: hug.types.text,
                 label: hug.types.text,
                 name: hug.types.text,
                 order,
                   ):
        """This method send an email to customer and notify him.
        Args:
            to_emails (str) : email of customer
            name (str): name of customer
            label (str): link to label of shipping
        Return:
            state (str): return starus code of response
        """
        state = notifications_rpc.send_email_with_temp(to_email, label, name, order)
        return state

    @hug.object.post('/api/notifications/sms/')
    def send_sms(
                self,
                number: hug.types.text='+79994413746',
                content: hug.types.text="Your Order is ready",
                ):
        """This method send SMS to a customer and notify him
        Args:
            number (str): number of customer. Number can be valid.
            content (str): message in sms
        Return:
            state(str): return starus code of response
        """
        state = notifications_rpc.send_sms(number, content)
        return state
