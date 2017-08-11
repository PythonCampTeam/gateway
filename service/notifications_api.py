import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings


class NotificationsAPI(object):
    @hug.object.get('/api/notifications',
                    examples='name=NoteBook&category=Dell')
    def shipments(self, name: str):
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.ShippingRPC.service_state(name=name)
            state2 = rpc.ShipingRPC.__doc__
        return {name: state, '42': state2}

    @hug.object.post('/api/notifications/email/{email}',
                     examples='email=tamara.mallysheva@saritasa.com')
    def send_email(self, email):
        # to_email = kwargs.get("email")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.send_email(email)
        return state

    @hug.object.post('/api/notifications/sms/{number}',
                     examples='+79994413746')
    def send_sms(self, number):
        # number = kwargs.get("number")
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.NotificationsRPC.sms(number)
        return state
