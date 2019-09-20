# Pizza Ordering Service

This project uses the Django REST Framework to implement an API for ordering pizza. I completed it as an assignment for a job application. It mainly focuses on code structure and data modeling skills.

## Installation

Checkout this project and perform the following steps:

1. Navigate to your project directory, and setup a virutalenv on your machine: `python3 -m venv env` and then activate the environment: `source env/bin/activate`
2. Install the libraries in the requirements.txt file: `pip install -r requirements.txt`
3. In a new terminal window, run postgres and execute the queries listed in the ***dbscripts/create_roles.sql*** file.
4. Once your database and roles have been created, we'll need to run the migrations from the project. In your terminal where you activated your virtual environment, cd to the *pizzaproject* directory and run `python3 manage.py migrate` to setup your tables.
5. Returning back to your postgres terminal window, run the queries in the ***dbscripts/populate_db.sql*** file to populate the tables with sample data.

Once your tables have been populated, we can run the application and start sending requests: `python3 manage.py runserver` and you will see the following output:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 20, 2019 - 13:23:19
Django version 2.2.5, using settings 'pizzaproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Usage
Please familiarize yourself with the models in the ***models*** directory so you get a sense of the relationships between the different tables. From a high level overview, an Order is consisted of one or more Pizzas, which is consisted of one or more Ingredients. An Order also contains a customer. A few sample request files have been provided in the ***samples*** directory.

## Endpoints
GET ***/order*** - displays all of the orders in the system (returning limited fields)

POST ***/order*** - creates a new order

GET ***/order/:id*** - retrieves an order and all its fields

POST ***/order/:id*** - updates an order

DELETE ***/order/:id*** - deletes an order

GET ***/order/:id/status*** - retrieves the status of an order

POST ***/order/:id/status*** - updates the status of an order

## Project Structure
```bash
.
├── manage.py
├── pizzaapp
│   ├── admin.py
│   ├── apps.py
│   ├── dbscripts    # sql scripts
│   ├── migrations   # migration files
│   ├── models       # models files
│   ├── sample       # sample json files
│   ├── serializers  # serializers
│   ├── services     # service classes
│   ├── tests.py     # tests file
│   ├── urls.py      # pizza app urls file
│   └── views        # views
├── pizzaproject
│   ├── settings.py  # project settings file
│   ├── urls.py      # project urls file
│   └── wsgi.py
└── requirements.txt
```

## Tests
You can run the tests within the ***tests.py*** file by using `python3 manage.py test` in the project folder. Example output:

```python
(env) MacBook-Pro:pizzaproject$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.030s

OK
Destroying test database for alias 'default'...
```

## Further considerations
This project was developed under time constraints, and the main objectives were to demonstrate project structuring, code layering and database modelling skills. Given more time, certain things such as validators, additional business layer logic and proper order numbering/customer numbering logic would be implemented.