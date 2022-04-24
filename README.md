**PYtech: Django And Celery Task** <br />

**Steps to run:** <br />
1- Install all requirements using 'pip install -r requirements.txt'<br />
2- Add .env file next to manage.py file <br />
3- Set environment  using env.example <br />
4- Set Broker URL in .env file <br />
5- Cd to root folder then run migrate command 'python manage.py migrate' <br />
6- Start Broker and set broker url in .env file with CELERY_BROKER_URL name <br />
7- Start celery using command 'celery --app=config worker --loglevel=info --logfile=logs/celery.log' <br />
8- Run scripts using 'python manage.py runscript **name_of_script**' <br />
9- Run tests using 'python manage.py test' to test the behavior <br /> <br />

**Notes:** <br />
1- Script slow_iteration takes argument to change the 50 records number using command 
'python manage.py runscript slow_iteration --script-args num 50'
the default num value is 50. <br />

2- When you run django and celery project project will create logs folder at the root
contains django.log file and celery.log file to write logs of servers
to follow the logs you can use 'tail -f path_to_your_project/logs/name_of_log_file.log' <br />

3- I used django_extensions for script running I think we can add command by extend base command
to add new command to manage.py and use it to run scripts. <br />

4- Set WORKING_SETTINGS to DEV if you are using local environment and add in settings/dev.py your settings <br />

5- Custom Admin Panel to check Results and data <br /> <br />


**BY Eng. Ali Askar**