**_ for PYtech: Django And Celery Task_**

**Steps to run:**
1- Install all requirements using 'pip install -r requirements.txt'
2- add .env file next to manage.py file
3- set environment  using env.example 
4- set Broker URL in .env file
5- cd to root folder then run migrate command 'python manage.py migrate'
6- start Broker and set broker url in .env file with CELERY_BROKER_URL name
7- start celery using command 'celery --app=config worker --loglevel=info --logfile=logs/celery.log'
8- run scripts using 'python manage.py runscript **name_of_scripy**'
9- run tests using 'python manage.py test' to test the behavior

**Notes**
1- slow_iteration scripy take argument to change the 50 records number using command
'python manage.py runscript slow_iteration --script-args num 50'
the default num value is 50.

2- when you run django and celery project will create logs folder at the root
contains django.log file and celery.log file fot write logs of servers
follow the logs using 'tail -f path_to_your_project/logs/name_of_log_file.log'

3- I used django_extensions for script running I think we can add command by extend base command
to add new command to manage.py and use it to run scripts.

4-set WORKING_SETTINGS to DEV if you are using local environment and add in settings/dev.py your settings

**BY Eng .Ali Askar**