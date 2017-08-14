from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='ShippingRPC')
# here init methods for use
service_state = rpc_service.method_rpc(method_name='service_state')
