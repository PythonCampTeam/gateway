import hug
from service.gateway import Products

route = hug.route.API(__name__)
route.object('/api/products')(Products)