from operator import getitem
from nameko.standalone.rpc import ClusterRpcProxy
# try:
#     from config.settings.common import security as security_settings
# except ImportError:
#     from gateway.config.settings.common import security as security_settings

AMQP_CONFIG = {'AMQP_URI': "amqp://guest:guest@rabbit"}


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
    def __init__(self, service_name=None):
        self.rpc_cluster = ClusterRpcProxy(AMQP_CONFIG)
        self.service_name = service_name
        self.rpc_proxy = self.rpc_cluster.start()

    def method_rpc(self, method_name=None):
        if method_name:
            service = getitem(self.rpc_proxy, self.service_name)
            return getattr(service, method_name)
        else:
            raise AttributeError('The attribute method_name will not empty')
