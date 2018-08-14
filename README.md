# Papyrus

A app for requesting a new feature on a software.

The app is available [here](https://lele-papyrus.herokuapp.com/).


## Development

### Technologies

* Python 3.7
* Pipenv version 2018.6.25
* Django 2.1 for main process
* Restless 2.1.1 for API definitions
* HTML + Bootstrap + Vue Js for frontend pages
* pytest + pytest-django + factories for tests

Decoupled frontend using [Vue Js](https://vuejs.org/).

### Run

To run the app, you should you pipenv and you must have Python 3.7 installed.
For detailed instructions on how to use pipenv check 
[this](https://docs.pipenv.org/).

To run the app locally, you must copy the `env-template` file to a `.env` file.

The default configuration is defined for using `sqlite`. If you want to 
use PostgreSQL, please provide the 
[database URL](https://github.com/kennethreitz/dj-database-url#url-schema)
 in a variable called `DATABASE_URL` inside the `.env` file.

To run the Django app run:

```sh
$ pipenv run python papyrus/manage.py runserver
```

And the app will run on `localhost:8000`.

To run the tests:

```sh
$ pipenv run pytest papyrus
```

## System Docs

The user can access 3 webpages:

* `/`  : have the table with all features registred on the system ordered by 
target date
* `/add/` : a page where the user can add a new feature
* `/detail/<id>/` : a detailed view of the feature with the id

The API has a single endpoints:

* a GET on `/api/features/` will give you all available features registred
* a GET on `/api/features/<id>/` will give a specific feature
* a POST on `/api/features/` will create a new feature if all informations are given

The POST request must have the following inputs:

* Title - short description of the request
* Description - a detailed description of request
* Priority - an integer that defines the priority of the feature for that specific 
customer
* Target date - a date when the feature should be delivered (yyyy-mm-dd)
* Client - one of the clients registred (available: 'A' to 'D')
* Product area - which area of business the feature will be add (available: '1' to '4')

The inputs must be sent as a json file such as:

```json
{
    "client": "A",
    "target-date": "2018-08-08",
    "product_area": "1",
    "title": "My Title",
    "description": "My description",
    "priority": "1"
}
```

## Features not added in current version of Papyrus

* User authentication for creating a new feature
* Pagination for both the API and frontend
