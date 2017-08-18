from integration import rpc_service as rpc

"""
   Initialize RPC service here for integrated in hug api
"""

rpc_service = rpc.ServiceRPC(service_name='NotificationsRPC')
# here init methods for use
testing = rpc_service.method_rpc(method_name='testing')
send_email = rpc_service.method_rpc(method_name='send_email')
send_sms = rpc_service.method_rpc(method_name='send_sms')
