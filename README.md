# cars_django


This API handles information about cars and its users

## How to run

#### 1) cd django_cars/carSite 
#### 2) python manage.py runserver 

### How to test

Admin:
http://127.0.0.1:8000/admin/
user: admin
password: secretpass



## cars_users API

Go to
http://127.0.0.1:8000/
http://127.0.0.1:8000/cars_users/
or 

```
curl -X GET http://127.0.0.1:8000/cars_users/
```


```
curl -X POST http://127.0.0.1:8000/cars_users/ -H 'Content-Type: application/json ' -d 
'{
    "name": "Jhon",
    "email": "test@test.com",
    "phone" : "1234567"
}'
```
Response

```
[
    {
        "id": 1,
        "created_at": "2020-06-02T02:35:33Z"
    },
    {
        "id": 2,
        "created_at": "2020-06-02T02:39:34Z"
    }
]
```


## ford Cars API

Go to http://127.0.0.1:8000/get_ford_cars/

or 

```
curl -X GET http://127.0.0.1:8000/get_ford_cars/?list_length=100
```


### TODO
 
 first: Update this README.md file everytime

1) Add the following APIs 
   - 1.1) POST users. Validate format
   - 1.2) GET user by ID
   - 1.3) PUT users. Validate format
   - 1.4) PATCH users. Validate format
   - 1.5) DELETE users
   - 1.6) GET ALL users
   - 1.7) Same for Cars API
   - 1.8) GET Healtcheck
   - 1.9) Add Swagger
2) Add UT
    - 2.1 Use Mock libraries
    - 2.2 Use Stubbers
3) Add ST
    - 3.1 Use Mock server. Something like pretenders
4) Add contract test
5) Implement some free CI/CD. Check gitlab
6) Dockerize. Store in docker hub
7) Add authentication
    - 7.1) Implement OpenID-Connect
    - 7.2) Use JWT
8) Add postgres
9) Add another Non-SQL DB
    - 9.1) Test registers users in Mongo
    - 9.2) Test some K-V (redis)
10) Add Apache or Gurnicorn
11) Add integration with some AWS service.
    - 11.1) Store users or cars in S3
    - 11.2) Try a lambda function just for apply some put
    - 11.3) Test SQS
    - 11.4) Test ECS
    - 11.5) Test DynamoDB
    - 11.6) Test Cognito
12) Implement K8s
    - 12.1) Test some deployment service (such as AWS)
    - 12.2) Test replication
    - 12.3) Use Helm
13) Add lint or another static analysis tool
14) Test some email notification service
15) Add notification API to SLACK
16) Test RabbitMq and Celery
