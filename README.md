# XMarksTheSpot

The focus of this project is to design a tool that allows Xavier students to reserve study rooms in all buildings on campus.
Greater efficiency in scheduling and reserving study rooms should give Xavier students more control over studying and
organizing group projects. Further, we expect this tool to more efficiently distribute study rooms during high-demand
times during the semester. The tool will be platform independent to allow universal access for all students and will
consist of a website.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

Django - use online directions from reliable sources that best fits your system and downloading files from
https://www.djangoproject.com/download/

mySQL - use online directions from https://www.mysql.com/downloads/

### Installing

A step by step series of examples that tells you how to get a development env running

Clone repo on desired file:
```
$ git clone https://github.com/nelsona11/XMarksTheSpot.git
```

Go into file directory of XMarksTheSpot and into branch titles PetersBranch2.

  In terminal:
```
$ cd XMarksTheSpot
$ cd git checkout PetersBranch2
```


First, update settings.py and firstCleanDatabase.py file in XMarksTheSpot file to access your MySQL using your mySQL account information. NOTE: You MUST have VERY high privileges to run the setup.py file. This may be done by running as root and setting that as your user in the following files.

  In terminal:
```
$ cd XMarksTheSpot
$ open settings.py
```
  Once opened, edit lines 86-87 where USER and PASSWORD fields are your own.
  Save.

  Next, in terminal:
```
$ cd ..
$ open firstCleanDatabase.py
```
  Once opened, edit line 5 where host, user, passwd are your own.
  Save.

Next, we need to setup database and create an admin account.

  In terminal type the following and follow commands to setup
  an admin user:
```
$ python setup.py
```

Lastly, to run server locally do the following.

  In terminal:
```
$ python manage.py runserver
```

## Iteration 1 Function Tests

Use link displayed in terminal to see website.


Create accounts.


Login to accounts.


See user accounts by accessing the /admin page logging in as admin user that was created with setup.py was ran.

## Iteration 2 Function Tests

Use tabs displayed above to toggle through the webpages on the website.

Create rooms by accessing the /admin page logging in as admin user that was created with setup.py was ran.

First, you must add the Building(s), then add Floor(s), then add Room(s).

After these have been created, you can view the site again and they should be present under the /buildings page.


In addition, after you are logged in, you can make hourly reservations. This is done via 2 ways.


    Via the /buildings page.

        They can select the desired building that will lead to selecting the desired floor of that building. Secondly, it will lead to selecting the desired room in that floor.
        Once the room is select, the reservation page should appear.
        Here, you can reserve in the following format:
                Monday
                6
                pm


        Once information is submitted, a message will appear that it was successful or that a the room has already been reserved.


    Via the /available page.

            They can select the desired building's room.
            Once the room is select, the reservation page should appear.
            Here, you can reserve in the following format:
                    Monday
                    6
                    pm


            Once information is submitted, a message will appear that it was successful or that a the room has already been reserved.  


In addition, /available page should only display rooms that are not reserve at the current time.
This can be checked by making a reservation for the current hour and seeing that it is not displayed in the /available page anymore.


Lastly, one can see a list of the reservations they made by accessing the /profile page if they're signed in.

## Built With

* [Django](https://www.djangoproject.com) - The web framework used
* [mySQL](https://www.mysql.com) - Used to generate database

## Authors

* **Andrew Nelson** - *Initial work* - [nelsona11](https://github.com/nelsona11)
* **Yasmin Alvarado-Rayo** - *Initial work* - [YasminAR16](https://github.com/YasminAR16)
* **Santiago Salazar** - *Initial work* - [Salazars1](https://github.com/Salazars1)
* **Chris Sievers** - *Initial work* - [sieversc](https://github.com/sieversc)
* **Sammy Fox** - *Initial work* - [smfox7](https://github.com/smfox7)

See also the list of [contributors](https://github.com/nelsona11/XMarksTheSpot/contributors) who participated in this project.
