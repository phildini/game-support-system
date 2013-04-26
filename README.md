game-support-system
===================

To install:
- Setup a virtualenv in the top directory: $ virtualenv .
- Install requirements: $ pip install -r rquirements.txt
- cd into the django project directory: $ cd game-support-system
- start the server: $ python manage.py runserver

The Game Support System is now running.
Feel free to browse to the following urls to play with it:
(You will have to login with user:kixeye, pass:kixeye)
- http://localhost:8000/users
- http://localhost:8000/users/<user_id>
- http://localhost:8000/users/search?nickname='philip'
- http://localhost:8000/battles
- http://localhost:8000/battles/<battle_id>

In a separate terminal, you can also run 'python test_system.py' to see some of
the basic API features. 

NOTE: Browsing by battle start and end time not currently implemented.