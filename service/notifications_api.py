import hug
import json
from integration import notifications_rpc


class NotificationsAPI(object):
    @hug.object.get('/api/notifications',
                    examples='name=NoteBook&category=Dell')
    def shipments(self, name: str):
        state = notifications_rpc.testing(name=name)
        state2 = notifications_rpc.__doc__
        return {name: state, '42': state2}

    @hug.object.post('/api/notifications/email/send')
    def send_email(self, body):
        """This method send an email to customer and notify him.
        Args:
            body (dict):  contain fields: to_email, subject, body, from_email
        """
        # to_email = kwargs.get("email")
        convert = dict(body)
        to_email = convert.get("to_email")
        from_email = convert.get("from_email")
        subgect = convert.get("subject")
        content = convert.get("content")

        state = notifications_rpc.send_email(to_email,
                                             from_email,
                                             subgect,
                                             content
                                             )
        return json.dumps(state)

    @hug.object.post('/api/notifications/Messages/')
    def send_sms(self, body):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, content
        """
        # number = kwargs.get("number")
        convert = dict(body)
        to_phone = convert.get("to_phone")
        content = convert.get("content")
        state = notifications_rpc.send_sms(to_phone, content)
        return json.dumps(state)
