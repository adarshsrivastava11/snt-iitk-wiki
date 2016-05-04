SNT-IITK-Wiki
=============

A campus-wiki setup for IIT Kanpur, written in Django.

## Test plan
Use python-2.7. So if `python --version` returns a python version different from 2.x, use `python2` and `pip2` in the following commands.
```
sudo pip install django
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```

Visit `localhost:8000/admin` and create a new team first, which will let you create test accounts.
