# Pricing Module
This is a Django App with a configurable pricing module and Fare Calculation
Django-Admin is used for giving Front-end UI
Postgres is used for Database related operations

## Installation
Follow the below steps to run the app:-

1. Clone the repo in your local env
2. Set the environment variables present in .env file accordingly
3. Set a python virtual Env
4. Execute Command (pip install -r requirements.txt) to install all the dependencies
5. Create Migrations files using command (python manage.py makemigrations)
6. Execute these Migrations file using command (python manage.py migrate)
7. Now create a superuser using command (python manage.py createsuperuser)
8. To start the server execute command (python manage.py runserver)

## Usage
Follow the below steps to see the working:-

1. Now visit this url (localhost:{port}/admin/) through a browser and login through the superuser creds.
2. Add values for pricing configurations
3. Finally, hit a get request at this url (localhost:{port}/pricing/calc_fare/) with distance value in request body.
