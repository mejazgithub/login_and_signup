# login_and_signup using django rest framework

APIs of User registration and Login with API key authentication and access token authentication 
using rest_framework, rest_framework_simple_jwt and rest_framework_apikey.

# 1. Create a virtual enviroment and activate it 

# 2. install requirement.txt using command 
     
     pip install -r requiremnet.txt

# 3. Run migrations using command
    
    1. python manage.py makemigrations
    2. python manage.py migrate

# 4. Create a super user using command 
     python manage.py createsuperuser

# 5. Runserver and login to admin panel

# 6. create an apikey using ApiKey model from admin panel 

# 7. copy the apikey and add it into your header with Apikey prefix 
     
     1. for example:  headers = {"apikey": "Api-Key yourapikey"}
     
     2. if you are using postman
     <img src="![apikey-example](https://user-images.githubusercontent.com/75315169/186418311-11966c83-7170-4e26-bb18-766d58803424.png)" alt="Alt text" title="Optional title">
     
# 8. hit the URL's

    1. http://localhost:8000/api/accounts/signup/  for creating a user 
    2. http://localhost:8000/api/accounts/signin/  for sign in

