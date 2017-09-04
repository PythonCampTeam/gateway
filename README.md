### Micro-services
Simple product e-commerce set of micro services (list products, buy, checkout, shipping, notifications), which are capable to communicate between themselves in order to achieve loose coupling.
# Micro-services uses a number of open source projects to work properly:
  - [Hug API](https://github.com/timothycrosley/hug)
  - [Cerberus](https://github.com/pyeve/cerberus)
  - [Nameko](https://github.com/nameko/nameko-examples)
  - [Shippo](https://github.com/goshippo/shippo-python-client)
  - [Twilio](https://github.com/twilio/twilio-python)
  - [Sendgrid](https://github.com/sendgrid/sendgrid-python)
  - [Stripe](https://github.com/stripe/stripe-python)

#### Services "Products"
***
Service based by software platform for internet commerce
[StripeAPI](https://stripe.com/)
The built-in database is used by [StripeAPI](https://stripe.com/)
More about [Stripe](https://stripe.com/docs/api)
***
This service performs functions:
  - Create new products and SKU
  -  Update product
  -  Retrieve list of products with sorted and filter
  -  Delete product by id
  -  Get information about product by id

### Create new products

Examples post request
```sh
POST /api/products/
```
```sh
{
      "name": "Wally bone",
      "description" : "The best gift for your pet",
      "attributes" : ["manufacturer",
                          "material"],
      "package_dimensions" :  {"height": 5.0, "length": 5.0,
                               "weight": 5.0, "width": 5.0},
      "metadata": {
      "category": "food",
      "for": "cats",
      "type": "fish"
      },
      "attributes_sku": {
      "manufacturer": "PetHappy",
      "material": "rubber"},
      "price": 50,
      "inventory":{
      "type": "finite",
      "quantity": 500
      }
}
```
Returns a product object if the call succeeded.
See example [responce](https://stripe.com/docs/api#create_product)
### Update product
Examples put request
```sh
PUT /api/products/{id_product}
```
```sh
{
	"metadata": {"category": "toys", "for": "dogs", "type": "bone"},
	"name": "Test_put",
    "description": "For small dogs"
}
```
Returns the product object if the update succeeded.
See example [responce](https://stripe.com/docs/api#update_product)
### Retrieve list of products with sorted and filter
Examples get request
```sh
GET /api/products/?category=toys&order_by=name
```
The category parameter serves not only to filter the list, but also to search for a keyword.
See example [responce](https://stripe.com/docs/api#list_products)
### Delete product by id
```sh
DELETE /api/products/{id_product}
```
Returns an object with a deleted parameter on success. Otherwise, this call raises an error.
See example [responce](https://stripe.com/docs/api#delete_product)
