import hug
import falcon
from integration import notifications_rpc
import nameko


class NotificationsAPI(object):

    @hug.object.post('/api/notifications/email/')
    def send_email(self, body):
        """This method send an email to customer and notify him.
        Args:
            data (dict):  contain fields: to_email, subject, body, from_email
        """
        if body is None:
            return {"code": falcon.HTTP_400,
                    "error":
                    "Required fields to_phone, content"}
        state = notifications_rpc.send_email(body)
        return state

    @hug.object.post('/api/notifications/sms/')
    def send_sms(self, body):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, content
        """
        if body is None:
            return {"code": falcon.HTTP_400,
                    "error":
                    "Required fields to_phone, content"}
        state = notifications_rpc.send_sms(body)
        return state

    @hug.exception(nameko.exceptions.RemoteError)
    def handle_exception(exception):
        """Handles the provided exception for testing"""
        return {"messages": "O_o"}
