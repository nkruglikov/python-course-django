# Dummy forum

A homework for python course.

## How to test it

1. Ensure that ```virtualenv``` and ```pip``` are installed.
2. Clone repository and move to its directory.
3. Create virtualenv: ```virtualenv-3.4 .```
4. Activate it: ```source /bin/activate```). 
5. Install requirements: ```pip install -r requirements.txt```
6. Create database: ```forum/manage.py migrate```
7. Configure it: ```forum/manage.py syncdb```
8. Run server: ```forum/manage.py runserver```
9. Go to [```http://localhost:8000/```](http://localhost:8000/)
