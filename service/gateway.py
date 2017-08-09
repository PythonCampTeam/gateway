import hug
from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://guest:guest@rabbit"}


class Products(object):
    """ Class for make request on service products
    Args:
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/products', examples='name=NoteBook&category=Dell')
    def products(self, name: str):
        with ClusterRpcProxy(CONFIG) as rpc:
            hello = rpc.greeting_service2.hello(name=name)
        return {name: hello}
