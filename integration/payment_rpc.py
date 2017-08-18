from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='PaymentsRPC')

add_in_cart = rpc_service.method_rpc(method_name='add_in_cart')
get_cart = rpc_service.method_rpc(method_name='get_cart')
delete_item = rpc_service.method_rpc(method_name='delete_item')
update_item = rpc_service.method_rpc(method_name='update_item')
new_order = rpc_service.method_rpc(method_name='new_order')
pay_order = rpc_service.method_rpc(method_name='pay_order')
