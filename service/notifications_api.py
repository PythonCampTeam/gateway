import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings


class NotificationsAPI(object):
    @hug.object.get('/api/notifications',
                    examples='name=NoteBook&category=Dell')
    def shipments(self, name: str):
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.testing(name=name)
            state2 = rpc.NotificationsRPC.__doc__
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

        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.send_email(to_email, from_email,
                                                    subgect, content)
        return state

    @hug.object.post('/api/notifications/Accounts/{AccountSid}/Messages',
                     example='AccountSid=AC3adbfe0e72f9d7dc7197fefd2cab7aca')
    def send_sms(self, body):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, content
        """
        # number = kwargs.get("number")
        convert = dict(body)
        to_phone = convert.get("to_phone")
        content = convert.get("content")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.send_sms(to_phone, content)
        return state
