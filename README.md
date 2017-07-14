This is an example for an easy Django application. You can use this to find dates for meetings, parties or similar.

Installation
------------
You can host this application with or without a virtualenv. To create one type

    pyvenv env
    source env/bin/activate
    
while you are in the directory where your files should live. On a production server this is probably somewhere under 
/var/www on a developers machine this is normally somewhere in your $HOME.

Now you can clone the sourcecode of the application into your directory

    git clone git@github.com:pinae/django-dudel.git
    
After that you should have a subdirectory `dudel/` and if you created a virtualenv also a subdirectory `env/`. The
actual application is in the `dudel/` directory. So go there: `cd dudel/`.

Now you have the application itself but you need to initialize your database. You can canfigure `dudel/settings.py`
to use mySQL or PostGreSQL described 
[here](https://docs.djangoproject.com/en/1.11/ref/databases/ "Django database documentation"). 
Or you can leave the file as it is to use sqlite.

Initialize your database with

    ./manage.py migrate

Start a development Server
--------------------------
If you are testing the application or if you are a developer you can start the application now with

    ./manage.py runserver
    
The application can be accessed under the url `http://localhost:8000`.

Deployment on a production server
---------------------------------
As this application is directed at developers as an example of how to work with Django some development options are
activated by default. On a production server you should change these settings as they might expose information about
your server to possible attackers.

Edit `dudel/settings.py` and change `DEBUG` to `False`. In `settings.py` is also a 
[link](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/) to the Django documentation with tips for 
what to do on production servers.

There is wsgi file (`dudel/wsgi.py`) which you can use with a wsgi-server like 
[uwsgi](https://uwsgi-docs.readthedocs.org/en/latest/ "uwsgi website and documentation"). As this is dependant on
which webserver you use please refer to the documentation of your wsgi and webserver of your choice. We successfully 
tested this with uwsgi and nginx.
