import hug
import json
import falcon
from integration import notifications_rpc


class NotificationsAPI(object):

    @hug.object.post('/api/notifications/email/send')
    def send_email(self, data):
        """This method send an email to customer and notify him.
        Args:
            body (dict):  contain fields: to_email, subject, body, from_email
        """
        state = notifications_rpc.send_email(data)
        if state is False:
            return falcon.HTTP_400
        return state

    @hug.object.post('/api/notifications/Messages/')
    def send_sms(self, body):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, content
        """
        state = notifications_rpc.send_sms(body)
        return json.dumps(state)


body = {
	"to_email": "tamara.malysheva@saritasa.com",
	"from_email": "test@example.com",
	"subject" : "blabla",
	"content" : "content"
}
