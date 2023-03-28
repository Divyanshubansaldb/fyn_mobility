# Pricing Module
This is a Django App with a configurable pricing module and Fare Calculation
Django-Admin is used for giving Front-end UI
Postgres is used for Database related operations
Used kubernetes to deploy this application

## Installation
Follow the below steps to run the app:-

1. Clone the repo in your local env
2. Deploy the configmap using command (kubectl apply -f mobility-configmap.yaml)
3. Deploy the application and create pods using command (kubectl apply -f mobility-deployment.yaml)
4. Deploy the service using command (kubectl apply -f mobility-svc.yaml). This will enable you to forward the outside traffic to pods
5. Execute these Migrations file using command (python manage.py migrate)
6. Now create a superuser using command (python manage.py createsuperuser)

## Usage
Follow the below steps to see the working:-

1. Now visit this url (nodeip:{port}/admin/) through a browser and login through the superuser creds.
2. Add values for pricing configurations, User, Driver, Ride
3. Finally, hit a get request at this url (nodeip:{port}/pricing/calc_fare/) with start_time, end_time, start_km, end_km, user_id, driver_id in request body.
