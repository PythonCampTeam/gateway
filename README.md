### Micro-services

#### Products
#### Payments
#### Order
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


**Free Software, Hell Yeah!**
