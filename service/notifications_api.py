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
        email = convert.get("email")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.send_email(email)
        return state

    @hug.object.post('/api/notifications/sms/send')
    def send_sms(self, body):
        """This method send SMS to a customer and notify him
        Args:
            body (dict): contain fields: to_phone, subject, body
        """
        # number = kwargs.get("number")
        convert = dict(body)
        number = convert.get("number")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.send_sms(number)
        return state