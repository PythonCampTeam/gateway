import hug
from gateway import Products

route = hug.route.API(__name__)
route.object('/api/products')(Products)