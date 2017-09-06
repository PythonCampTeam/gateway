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
$ chmod ugo+x install_run_project
$ ./install_run_project
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
### Shipping
Service to create shipments over well-known carriers (like fedex or usps, dhl etc).
This service performs functions:
 - Create new shipment
 - List of existing shipments, stored in list of dicts
 - Get rate for the shipment
 - Generate shipping label

### Tech
Shipping microservice uses a  free account of Shippo
 - [Shippo](goshippo.com) shipping for platforms, marketplaces and ecommerce

### API endpoints
### Create new shipment
 Method work with stripe service when create order
 ```sh
POST /api/shipments/
 ```
Example [query](https://stripe.com/docs/orders/dynamic-shipping-taxes#order-creation-event)
Returns the order data updated rates and create shipments
```sh

  {
        "id": "or_1AyepaBqraFdOKT2ahMQkRsd",
        "object": "order",
        "amount": 446,
        "amount_returned": null,
        "application": null,
        "application_fee": null,
        "charge": null,
        "created": 1504609378,
        "currency": "usd",
        "customer": null,
        "email": "varvara.malysheva@saritasa.com",
        "items": [
            {
                "object": "order_item",
                "amount": 100,
                "currency": "usd",
                "description": "Wally pick",
                "parent": "sku_BLL1Ah7Wbdv2Zg",
                "quantity": 2,
                "type": "sku"
            },
            {
                "object": "order_item",
                "amount": 0,
                "currency": "usd",
                "description": "Taxes (included)",
                "parent": null,
                "quantity": null,
                "type": "tax"
            },
            {
                "object": "order_item",
                "amount": 346,
                "currency": "usd",
                "description": "First-Class Package/Mail Parcel",
                "parent": "8da5b27dfd87444cb752e63a378469d0",
                "quantity": null,
                "type": "shipping"
            }
        ],
        "livemode": false,
        "metadata": {},
        "returns": {
            "object": "list",
            "data": [],
            "has_more": false,
            "total_count": 0,
            "url": "/v1/order_returns?order=or_1AyepaBqraFdOKT2ahMQkRsd"
        },
        "selected_shipping_method": "8da5b27dfd87444cb752e63a378469d0",
        "shipping": {
            "address": {
                "city": "San Jose",
                "country": "US",
                "line1": "1092 Indian Summer Ct",
                "line2": null,
                "postal_code": "95122",
                "state": "CA"
            },
            "carrier": null,
            "name": "Chloe Taylor",
            "phone": null,
            "tracking_number": null
        },
        "shipping_methods": [
            {
                "id": "8da5b27dfd87444cb752e63a378469d0",
                "amount": 346,
                "currency": "usd",
                "delivery_estimate": {
                    "date": "2017-08-28",
                    "type": "exact"
                },
                "description": "First-Class Package/Mail Parcel"
            },
            {
                "id": "8da5b27dfd87444cb752e63a378469d0",
                "amount": 346,
                "currency": "usd",
                "delivery_estimate": {
                    "date": "2017-08-28",
                    "type": "exact"
                },
                "description": "First-Class Package/Mail Parcel"
            },
            {
                "id": "8da5b27dfd87444cb752e63a378469d0",
                "amount": 346,
                "currency": "usd",
                "delivery_estimate": {
                    "date": "2017-08-28",
                    "type": "exact"
                },
                "description": "First-Class Package/Mail Parcel"
            },
            {
                "id": "8da5b27dfd87444cb752e63a378469d0",
                "amount": 346,
                "currency": "usd",
                "delivery_estimate": {
                    "date": "2017-08-28",
                    "type": "exact"
                },
                "description": "First-Class Package/Mail Parcel"
            }
        ],
        "status": "created",
        "status_transitions": {
            "canceled": null,
            "fulfiled": null,
            "paid": null,
            "returned": null
        },
        "updated": 1504609382,
        "upstream_id": "1bd3fc762b69458491aea5fcb665dfc5"
    }
```
### Get list of existing shipments
Get request
```sh
GET /api/shipments/
```
Example response
```sh
[
    {
        "object_id": "1bd3fc762b69458491aea5fcb665dfc5",
        "address_to": {
            "name": "Chloe Taylor",
            "street1": "1092 Indian Summer Ct",
            "city": "San Jose",
            "state": "CA",
            "zip": "95122",
            "country": "US",
            "phone": null,
            "email": "varvara.malysheva@saritasa.com"
        }
    }
]
```
### Get rate for the shipment
Example request
```sh
GET /api/shipments/ID/rates/usd
```
Example response
```sh
{
    "object_id": "07712983ea1d45709c86e4d4d644e735",
    "rate_items": [
        {
            "object_id": "45006edb7a9d43e68ec2fe9faf99fa0e",
            "arrives_by": null,
            "zone": "1",
            "object_owner": "varvara.malysheva@saritasa.com",
            "provider_image_200": "https://shippo-static.s3.amazonaws.com/providers/200/USPS.png",
            "currency_local": "USD",
            "attributes": [
                "FASTEST"
            ],
            "currency": "USD",
            "amount": "21.18",
            "duration_terms": "Overnight delivery to most U.S. locations.",
            "servicelevel": {
                "name": "Priority Mail Express",
                "token": "usps_priority_express",
                "terms": ""
            },
            "provider_image_75": "https://shippo-static.s3.amazonaws.com/providers/75/USPS.png",
            "object_created": "2017-09-05T12:20:36.546Z",
            "shipment": "07712983ea1d45709c86e4d4d644e735",
            "estimated_days": 1,
            "test": true,
            "amount_local": "21.18",
            "messages": [],
            "provider": "USPS",
            "carrier_account": "c7d72d2025f740d89bdfb00f33c5d67a"
        },
        {
            "object_id": "c0716801a9c648e2a6f167aab639dcfb",
            "arrives_by": null,
            "zone": "1",
            "object_owner": "varvara.malysheva@saritasa.com",
            "provider_image_200": "https://shippo-static.s3.amazonaws.com/providers/200/USPS.png",
            "currency_local": "USD",
            "attributes": [],
            "currency": "USD",
            "amount": "5.84",
            "duration_terms": "Delivery within 1, 2, or 3 days based on where your package started and where it’s being sent.",
            "servicelevel": {
                "name": "Priority Mail",
                "token": "usps_priority",
                "terms": ""
            },
            "provider_image_75": "https://shippo-static.s3.amazonaws.com/providers/75/USPS.png",
            "object_created": "2017-09-05T12:20:36.545Z",
            "shipment": "07712983ea1d45709c86e4d4d644e735",
            "estimated_days": 2,
            "test": true,
            "amount_local": "5.84",
            "messages": [],
            "provider": "USPS",
            "carrier_account": "c7d72d2025f740d89bdfb00f33c5d67a"
        },
        {
            "object_id": "9777ec3a50164246981e5e3e1f2f6873",
            "arrives_by": null,
            "zone": "1",
            "object_owner": "varvara.malysheva@saritasa.com",
            "provider_image_200": "https://shippo-static.s3.amazonaws.com/providers/200/USPS.png",
            "currency_local": "USD",
            "attributes": [],
            "currency": "USD",
            "amount": "5.95",
            "duration_terms": "Delivery in 2 to 8 days.",
            "servicelevel": {
                "name": "Parcel Select",
                "token": "usps_parcel_select",
                "terms": ""
            },
            "provider_image_75": "https://shippo-static.s3.amazonaws.com/providers/75/USPS.png",
            "object_created": "2017-09-05T12:20:36.544Z",
            "shipment": "07712983ea1d45709c86e4d4d644e735",
            "estimated_days": 7,
            "test": true,
            "amount_local": "5.95",
            "messages": [],
            "provider": "USPS",
            "carrier_account": "c7d72d2025f740d89bdfb00f33c5d67a"
        },
        {
            "object_id": "876b49492f2a4a2b8f0ec7445874606c",
            "arrives_by": null,
            "zone": "1",
            "object_owner": "varvara.malysheva@saritasa.com",
            "provider_image_200": "https://shippo-static.s3.amazonaws.com/providers/200/USPS.png",
            "currency_local": "USD",
            "attributes": [
                "BESTVALUE",
                "CHEAPEST"
            ],
            "currency": "USD",
            "amount": "3.46",
            "duration_terms": "",
            "servicelevel": {
                "name": "First-Class Package/Mail Parcel",
                "token": "usps_first",
                "terms": ""
            },
            "provider_image_75": "https://shippo-static.s3.amazonaws.com/providers/75/USPS.png",
            "object_created": "2017-09-05T12:20:36.544Z",
            "shipment": "07712983ea1d45709c86e4d4d644e735",
            "estimated_days": 5,
            "test": true,
            "amount_local": "3.46",
            "messages": [],
            "provider": "USPS",
            "carrier_account": "c7d72d2025f740d89bdfb00f33c5d67a"
        }
    ]
}
```
### Get rate for the shipment
Example request
```sh
GET /api/shipments/ID/label/
```
Example response, return link on paid order
```sh
{
    "object_id": "75d6fd77d64b4e969c6635dade379e5c",
    "label_url": "https://shippo-delivery-east.s3.amazonaws.com/9b4f93ccbd7a40c383a6cbfdbbca0c8e.pdf?Signature=wVtYerQ4YOVyq2%2Ft5gzK7ae4z%2BI%3D&Expires=1536153158&AWSAccessKeyId=AKIAJGLCC5MYLLWIG42A"
}
```
### Payments & Cart

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
Examples delete request
 ```sh
DELETE /api/cart/prod_BByyzCWSMmhL7R/
 ```
Response - return cart without this product
```sh
[]
```
#### Get cart
 Examples get request
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
 Examples delete request
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
If the order is successfully paid, the SMS and email notification is sent
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
