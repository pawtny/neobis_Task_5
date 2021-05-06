# CRMFood Application

This project is created in order to understand Simple REST API by using Django and Django Rest Framework.

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
*(Commands are written for Windows.)*

### Requirments

After downloading the repository, get virtual environment and activate it in your directory:
```
pip install virtualenv
python -m venv venv
venv\Scripts\activate
```

Now that you're inside a virtual environment, install project's package requirements:

```
pip install -r requirements.txt
```

## Getting started

There is an overview on how it works:
```
cd courses_app
python manage.py runserver
```
Go to localhost:
* for departments list to http://127.0.0.1:8000/departments/
* for departments detail to http://127.0.0.1:8000/departments/ {department_id}


## Built With

* [Django](https://docs.djangoproject.com/en/3.0/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) which was used in order to learn REST API

## Versioning

There are no other versions

## Authors

* <b>Sardar Sultanaliev</b> - *initial work* - [sultanaliev-s](https://github.com/sultanaliev-s)
