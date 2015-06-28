Homebroil: Home-cooked food on-demand
===================

Demo: http://beta.homebroil.com

This project was developed to create a "Uber for Food". Users can upload leftovers or newly created food and others nearby can order their food.
This is a work-in-progress. Pull requests welcome! Collaborators wanted.

This was built to work on your local machine, as well as OpenShift. To deploy to Openshift, first create a Django app. Pull down your base-code, overwrite your base-code with this code, and push back up. For some reason, using this repo as a source repo upon creation usually results in an error.

This is a Pinax-based Django App with Bootstrap.

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
