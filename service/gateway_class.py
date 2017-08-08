import hug
from nameko.standalone.rpc import ClusterRpcProxy


config = {
    'AMQP_URI': "pyamqp://guest:guest@rabbit"
}


@hug.get('/api/products', examples='name=NoteBook&model=Dell')
@hug.local()
def products(**kwargs):
    """function try get parameters for use in rpc"""
    name = kwargs.get('name')
    return rpc_greeting_service(name)


def rpc_greeting_service(name):
    """test rpc call from greeting_service working on shipping container"""
    with ClusterRpcProxy(config) as cluster_rpc:
        hello_res = cluster_rpc.greeting_service.hello.call_async(name=name)  # "hellø-x-y"
        hello_res2 = cluster_rpc.greeting_service2.hello.call_async(name=name)  # "hellø-x-y"
        print(hello_res.result())
        return {hello_res.result(), hello_res2.result()}

