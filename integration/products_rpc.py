from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='ProductsRPC')
# here init methods for use
getproduct = rpc.method_rpc(method_name='getproduct')
