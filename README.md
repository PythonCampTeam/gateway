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

#### Products
#### Payments
#### Order



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




#### Notifications
This microservice send notification by email and by SMS.

  - Using account in Twilio for send sms.
  - Using account in Sendgrid for send emails.

# Expected API endpoints

  - **POST /api/notifications/email/**
  Send an email to customer and notify him. JSON payload contain fields: *to_email*, *subject*, *content*, *from_email*. Send emails in HTML format.
  - **POST /api/notifications/sms/**
Send SMS to a customer and notify him. JSON payload contain fields: *to_phone*, *content*.


This service performs functions:
  - Send sms to customer with information of status of order.
  - Send email to customer with information about order(label, cart and other).

### Tech

Notifications microservice uses a number of open source projects to work properly:

* [Sengrid](https://sendgrid.com/) - This library allows to quickly and easily use the SendGrid Web API v3 via Python.
* [Twilio](https://www.twilio.com/) - Library for easily send sms via Python.
* [Nameko](http://nameko.readthedocs.io/en/stable/) - A microservices framework for Python that lets service developers concentrate on application logic and encourages testability.
* [Hug](https://github.com/timothycrosley/hug) - Hug aims to make developing Python driven APIs as simple as possible, but no simpler.

And of course Notifications microservice itself is open source with a [public repository][dill]
 on GitHub.

 ### Sending mail

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
### Installation


Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Docker TODO
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```


### Todos

 - Write MORE Tests

License
----

MIT


**Free Software, Hell Yeah!**This microservice send notification by email and by SMS.

  - Using account in Twilio for send sms.
  - Using account in Sendgrid for send emails.

# Expected API endpoints

  - **POST /api/notifications/email/**
  Send an email to customer and notify him. JSON payload contain fields: *to_email*, *subject*, *content*, *from_email*. Send emails in HTML format.
  - **POST /api/notifications/sms/**
Send SMS to a customer and notify him. JSON payload contain fields: *to_phone*, *content*.


This service performs functions:
  - Send sms to customer with information of status of order.
  - Send email to customer with information about order(label, cart and other).

### Tech

Notifications microservice uses a number of open source projects to work properly:

* [Sengrid](https://sendgrid.com/) - This library allows to quickly and easily use the SendGrid Web API v3 via Python.
* [Twilio](https://www.twilio.com/) - Library for easily send sms via Python.
* [Nameko](http://nameko.readthedocs.io/en/stable/) - A microservices framework for Python that lets service developers concentrate on application logic and encourages testability.
* [Hug](https://github.com/timothycrosley/hug) - Hug aims to make developing Python driven APIs as simple as possible, but no simpler.

And of course Notifications microservice itself is open source with a [public repository][dill]
 on GitHub.

 ### Sending mail

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
### Installation


Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Docker TODO
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```


### Todos

 - Write MORE Tests

License
----

MIT


**Free Software, Hell Yeah!**
