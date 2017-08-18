import hug
from nameko.standalone.rpc import ClusterRpcProxy
from config.settings.common import security as security_settings
# from integration import products_rpc


class PaymentsAPI(object):
    """Class for created requests and worked with objects Products
        """
    @hug.object.get('/api/cart/',
                    examples='name=NoteBook&category=Dell')
    def test(self, name: str):
        with ClusterRpcProxy(security_settings.AMQP_CONFIG) as rpc:
            state = rpc.PaymentsRPC.add_in_cart()
        return {name: state}
