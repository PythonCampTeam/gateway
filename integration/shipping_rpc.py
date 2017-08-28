from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='ShippingRPC')
# here init methods for use
service_state = rpc_service.method_rpc(method_name='service_state')
shipping_get = rpc_service.method_rpc(method_name='shipments')

shipping_get_rates = rpc_service.method_rpc(method_name='shipments_rates')

shipping_order_update = rpc_service.method_rpc(method_name='shipments_create')
shipping_get_label = rpc_service.method_rpc(method_name='shipment_label')


