import nameko
from nameko.standalone.rpc import ClusterRpcProxy
from operator import getitem
from nameko.rpc import RpcProxy
from gateway.config.settings.common import security as security_settings


class ServiceRPC(object):
    """ helper for work with micro services
        Args:
            service_name(str): Name of service rpc
            method_name(str): Name of method from rpc service
        Return:
            func(function): method from service
        Example:
            needed_method = ServiceRPC(service_name='ShippingRPC',
                                       method_name='service_state')
            needed_method(id=42)
        ...{"id": 42}
    """
    def __init__(self, **kwargs):
        self.rpc_proxy = ClusterRpcProxy(security_settings.AMQP_CONFIG)
        self.rpc_proxy = self.rpc_proxy.start()
        self.service_name = kwargs.get('service_name')
        self.method_name = kwargs.get('method_name')

    def __call__(self):
        service = getitem(self.rpc_proxy, self.service_name)
        return getattr(service, self.method_name)


a = ServiceRPC(service_name='ShippingRPC', method_name='service_state')()
print(a(name='name'))
