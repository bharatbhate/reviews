# **Review API Test**

This Test serves APIs that allows users to post and retrieve their reviews of companies

### **Getting Started**

1. Clone the project

        git clone https://github.com/bharatbhate/reviews.git

2. Install the Requirements
    
        pip install -r requirements.txt
        
3. Do Migrations

        python manage.py makemigrations
        python manage.py migrate
        
4. Run the application

        python manage.py runserver
        
5. Below are the APIs to create user, login and add/retrieve reviews
    

## **API Documentation**
    
**Create User**
    
    
        curl -X POST \
        http://127.0.0.1:8000/reviews/create-user/ \
        -H 'Content-Type: application/json' \
        -d '{"username":"string",
            "password":"string"}'

_Response:_ 

Status: `201`

Body:
 
    {
        "id": integer,
        "username": "string"
    }


**User Login**
        
        
        curl -X POST \
        http://127.0.0.1:8000/reviews/api-token-auth/ \
        -H 'Content-Type: application/json' \
        -d '{"username":"string",
	        "password":"string"}'
	        
_Response:_ 

Status: `200`

Body:
 
    {
        "token": "string"
    }


**Add Reviews**
        
        
        curl -X POST \
        http://127.0.0.1:8000/reviews/ \
        -H 'Authorization: Token <Token string>' \
        -H 'Content-Type: application/json' \
        -d '{
            "title":"string",
	        "rating":integer,
	        "summary":"string",
	        "ip_address":"string",
	        "submission_date":"YYYY-MM-DD",
	        "company":"String"
        }'
	        
_Response:_ 

Status: `201`

Body:
 
    {
    "id": integer,
    "user": {
        "username": "string"
    },
    "title": "string",
    "rating": integer,
    "summary": "string",
    "ip_address": "string",
    "submission_date": "YYYY-MM-DD",
    "company": "String"
    }

**Get Reviews**
        
        
        curl -X GET \
        http://127.0.0.1:8000/reviews/ \
        -H 'Authorization: Token <Token String>' \
        -H 'Content-Type: application/json'
	        
_Response:_ 

Status: `200`

Body:
 
    [
        {
            "id": integer,
            "user": {
                "username": "string"
            },
            "title": "string",
            "rating": integer,
            "summary": "string",
            "ip_address": "string",
            "submission_date": "YYYY-MM-DD",
            "company": "String"
        }
    ]
    
    
  
## **Code Test and Coverage**

To run test cases:

    python manage.py test
    
To run test cases with coverage report:
    
    coverage run ./manage.py test &&
    coverage report

