#setup.py
#sets up a clean database (DBXMarksTheSpot) using sql file created for XMarksTheSpot
#sets up an admin user of user's choice from the beginning to access the database via the website
import firstCleanDatabase
import os

#migrate files
os.system("python manage.py migrate")

#prompts to create admin user
os.system("echo 'Create admin account to see users in database via web'")
os.system("python manage.py createsuperuser")
