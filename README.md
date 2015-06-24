You can run this code locally or on OpenShift in the Cloud

If you run this using OpenShift, you can keep code as-is and edit from there.

If you are running this locally, you will need to use mysql lite.

Please navigate to the wsgi/mysite/mysite/settings.py file and uncomment the first database array to be SQLite3.


If you are running this locally, here is some documentation from Pinax:

pinax-project-teams
===================

a starter project that has account management with profiles and teams
and basic collaborative content (wikis).



Usage:

    django-admin.py startproject -e py,.coveragerc --template=https://github.com/pinax/pinax-project-teams/zipball/master <project_name>


Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.5
    django-admin.py startproject -e py,.coveragerc --template=https://github.com/pinax/pinax-project-teams/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver