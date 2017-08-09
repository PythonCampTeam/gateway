import hug


class Products(object):
    """ Class for make request on service products
    Args:
        id(int): id products
        name(str): string name of products
        category(str): string name category of products
        """

    @hug.object.get('/api/products', examples='name=NoteBook&category=Dell')
    def products(self, name: str):
        return {name: name}
