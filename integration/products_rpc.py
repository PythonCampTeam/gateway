from gateway.integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='Productsrpc')
# here init methods for use

get_product = rpc_service.method_rpc(method_name='get_product')
create_product = rpc_service.method_rpc(method_name='create_product')
delete_product = rpc_service.method_rpc(method_name='delete_product')
update_product = rpc_service.method_rpc(method_name='update_product')
search_products = rpc_service.method_rpc(method_name='search_products')
get_sku_product = rpc_service.method_rpc(method_name='get_sku_product')
