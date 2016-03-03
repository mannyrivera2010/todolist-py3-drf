# todolist-py3-drf     [![Build Status][travis-image]][travis-url]
A sample todo list project to learn about Django REST Framework.

## TODO
 - Make vagrant box
 - Add Swagger 

## Concepts
- How DRF Work
- How Auth Work 
- REST

## Requirements
 - User is able to create many list
 - Lists can have many items
 - User can own Lists, not visible to other users
 - Items shall have a Title, Description, State (New, Done)

## Getting Started
The recommended approach is to use the vagrant box referenced, which will create a production-esque deployment of OZP:
* Postgres (vs. SQLite)
* HTTP Basic Auth
* Enable HTTPS (via nginx reverse proxy)
* Served via Gunicorn (vs. Django development server)

To serve the application on your host machine with minimal external dependencies, do the following:

1. Remove psycopg2 from requirements.txt (so that Postgres won't be required)
2. Enable HTTP Basic Auth and disable PKI authentication. In settings.py,
`REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES` should be set to
`'rest_framework.authentication.BasicAuthentication'`
4. In settings.py, set `TODOLIST.DEMO_APP_ROOT` to `localhost:8000` (or wherever
the django app will be served at)

Then, do the following:
1. Install Python 3.4.3. Python can be installed by downloading the appropriate
	files [here](https://www.python.org/downloads/release/python-343/). Note
	that Python 3.4 includes both `pip` and `venv`, a built-in replacement
	for the `virtualenv` package
2. Create a new python environment using python 3.4.x. First, create a new
	directory where this environment will live, for example, in
	`~/python_envs/ozp`. Now create a new environment there:
	`python3.4 -m venv ENV` (where `ENV` is the path you used above)
3. Active the new environment: `source ENV/bin/activate`
4. Install the necessary dependencies into this python environment:
	`pip install -r requirements.txt`
5. Run the server: `./restart_clean_dev_server.sh`

Swagger documentation for the api is available at `http://localhost:8000/docs/`
Use username `admin` password `password` when prompted for authentication info

There's also the admin interface at `http://localhost:8000/admin`
(username: `admin`, password: `password`)

## For Developers
This section should be helper for developers    
Developer shall be familiar with
 - Python 3
 - REST
 - Django
 - Django REST Framework

## Notes
Some commands
````
 ~/programs/python343/python -m venv env    
source env/bin/activate
````

Followed http://www.django-rest-framework.org/tutorial/quickstart/    

 
