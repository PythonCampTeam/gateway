from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='ProductsRPC')
# here init methods for use

getproduct = rpc_service.method_rpc(method_name='getproduct')
create_product = rpc_service.method_rpc(method_name='create_product')
list_products = rpc_service.method_rpc(method_name='list_products')
delete_product = rpc_service.method_rpc(method_name='delete_product')
update_product = rpc_service.method_rpc(method_name='update_product')
filter_products = rpc_service.method_rpc(method_name='filter_products')
search_products = rpc_service.method_rpc(method_name='search_products')
sorted_products = rpc_service.method_rpc(method_name='sorted_products')
get_sku_product = rpc_service.method_rpc(method_name='get_sku_product')
