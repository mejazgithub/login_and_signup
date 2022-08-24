# login_and_signup using django rest framework

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

# 7. copy the apikey and add it into your header with Api-key prefix 
     
     1. for example:  headers = {"apikey": "Api-Key yourapikey"}
     
     2. if you are using postman
     https://user-images.githubusercontent.com/75315169/186418792-e540e80a-bee5-46a4-9aca-e241dd3a79b2.png

     
# 8. hit the URL's

    1. http://localhost:8000/api/accounts/signup/  for creating a user 
    2. http://localhost:8000/api/accounts/signin/  for sign in

