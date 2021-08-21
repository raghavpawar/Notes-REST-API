# Notes REST API

This is a Note Making API made using the django-rest framework. You can use it in your React/React-Native or a Flutter mobile/web app.


## Installation

#### Using Docker
Make sure you have docker installed.

Open your terminal inside `notes` directory and run the following command.
```sh
$ docker-build .
$ docker run -p 8000:8000 (first four digits of sha code)
```
Your backend will be sucessfully running at http://localhost:8000/

#### Without Using Docker

Open your terminal inside `notes` directory and run the following command.

```sh
$ cd notes
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Your backend will be sucessfully running at http://localhost:8000/ 

Test the API as you like it!❤