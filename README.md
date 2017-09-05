## Micro-services
Simple product e-commerce set of micro services (list products, buy, checkout, shipping, notifications), which are capable to communicate between themselves in order to achieve loose coupling.
#### Micro-services uses a number of open source projects to work properly:
  - [Hug API](https://github.com/timothycrosley/hug)
  - [Cerberus](https://github.com/pyeve/cerberus)
  - [Nameko](https://github.com/nameko/nameko-examples)
  - [Shippo](https://github.com/goshippo/shippo-python-client)
  - [Twilio](https://github.com/twilio/twilio-python)
  - [Sendgrid](https://github.com/sendgrid/sendgrid-python)
  - [Stripe](https://github.com/stripe/stripe-python)
  - [docker-compose](https://github.com/docker/compose)
  - [Docker](https://github.com/docker)
 ### Installation and start
Download or copy to yourself sh [file](https://yadi.sk/d/S55ue6f53McPtm)
Run this commands in directory, where will be stored "Micro-services"
```sh
chmod ugo+x install_run_project
./install_run_project
```

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
### Tech

Products microservice uses a Stripe free account:

* [Stripe](https://stripe.com/) - This library allows to quickly and easily use the Stripe API v3 via Python.

Products microservice itself is open source with a [public repository](https://github.com/PythonCampTeam/products) on GitHub.

#### API endpoints
#### Create new products

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
#### Update product
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
#### Retrieve list of products with sorted and filter
Examples get request
```sh
GET /api/products/?category=toys&order_by=name
```
The category parameter serves not only to filter the list, but also to search for a keyword.
See example [responce](https://stripe.com/docs/api#list_products)
#### Delete product by id
```sh
DELETE /api/products/{id_product}
```
Returns an object with a deleted parameter on success. Otherwise, this call raises an error.
See example [responce](https://stripe.com/docs/api#delete_product)




#### Notifications
***
This microservice send notification by email and by SMS.
  - Using account in Twilio for send sms.
  - Using account in Sendgrid for send emails.

This service performs functions:
  - Send sms to customer with information of status of order.
  - Send email to customer with information about order(label, cart and other)  in HTML format.
***
### Tech

Notifications microservice uses a Sendgrid free account and free Twilio account:

* [Sengrid](https://sendgrid.com/) - This library allows to quickly and easily use the SendGrid Web API v3 via Python.
* [Twilio](https://www.twilio.com/) - Library for easily send sms via Python.

Notifications microservice itself is open source with a [public repository](https://github.com/PythonCampTeam/notifications) on GitHub.

#### API endpoints
 ### Sending mail
JSON payload contain fields: to_email, subject, content, from_email
 Examples post request
 ```sh
 POST /api/notifications/email/
 ```


 ```sh
 {
	"to_email": "tamara.malysheva@saritasa.com",
	"from_email": "test@example.com",
	"subject" : "blabla",
	"content" : "content"
}
```
Response
```sh
{"status code": "202"}
```

### Sending sms
JSON payload contain fields: to_phone, content.
 Examples post request
 ```sh
 POST /api/notifications/sms/
 ```
 ```sh
 {
    "number": +79994413746,
    "content": "Your order is ready!"
}
```


### Payments
Service that implements shopping cart with an in-memory database for products added to the cart and integrates with Stripe to process payments for a purchase of products.
This service performs functions:
 - Put product in cart, with quantity
 - Get all products in cart
 - Update quantity of given product in the cart
 - Delete product from the cart
 - Delete all products from the cart
 - Сreate order
 - Paid order
 - Change shipping method for order

### Tech

Payments microservice uses a Sendgrid all the above-mentioned microservices.
Database is in-memory dict.
Payments microservice itself is open source with a [public repository](https://github.com/PythonCampTeam/payments) on GitHub.
#### API endpoints
#### Add product in cart
 Examples post request
 ```sh
POST /api/cart/prod_BByyzCWSMmhL7R/buy/
 ```
 ```sh
 {
	"quality": 5
}
```
Response - return all cart
```sh
[
    {
      "type":'sku',
      "parent":'sku_BLHJWGDdPXTClG',
      "quality": 5
    }
  ]
```
#### Update product in cart
 Examples post request
 ```sh
PUT /api/cart/prod_BByyzCWSMmhL7R/
 ```
 ```sh
 {
	"quality": 1
}
```
Response - return all cart with update product
```sh
[
    {
      "type":'sku',
      "parent":'sku_BLHJWGDdPXTClG',
      "quality": 1
    }
  ]
```
#### Delete product in cart
 Examples post request
 ```sh
DELETE /api/cart/prod_BByyzCWSMmhL7R/
 ```
Response - return cart without this product
```sh
[]
```
#### Get cart
 Examples post request
 ```sh
GET /api/cart/
 ```
Response - return all  cart
```sh
[
    {
      "type":'sku',
      "parent":'sku_BLHJWGDdPXTClG',
      "quality": 1
    }
  ]
```
#### Delete all  cart
 Examples post request
 ```sh
DELETE /api/cart/
 ```
Response - return empty cart
```sh
[]
```
#### Create order
 Examples post request
 ```sh
POST /api/cart/checkout/
 ```
  ```sh
{
   "email": "varvara.malysheva@saritasa.com",
   "phone": "+79994413746",
   "name": "Chloe Taylor",

   "address":{
      "line1":"1092 Indian Summer Ct",
      "city":"San Jose",
      "state":"CA",
      "country": "US",
      "postal_code":"95122"
   }
}
 ```
Response - [the order object](https://stripe.com/docs/api/python#order_object)
#### Change shipping method
 Examples post request
 ```sh
POST /api/cart/shipping/
 ```
```sh
{
   "order_id": "or_1AxW4eBqraFdOKT2HIrPPf3m",
   "shipping_id": "e5d1b5f1101949d29271256d0159558f"
}
 ```
Response - [the order object](https://stripe.com/docs/api/python#update_order)
#### Paid order
 Examples post request
 ```sh
POST /api/cart/paid/
 ```
```sh
{
            "order_id": "or_1AxW4eBqraFdOKT2HIrPPf3m"
            "cart": "tok_mastercard"
}
 ```
Response - [the order object](https://stripe.com/docs/api/python#pay_order) with update status "paid", status code of send email and sms
