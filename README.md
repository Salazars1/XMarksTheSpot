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

A step by step series of examples that tell you have to get a development env running

Clone repo on desired file:
```
$ git clone https://github.com/nelsona11/XMarksTheSpot.git
```

In file directory of XMarksTheSpot after repository has been cloned:

  First, update settings.py and firstCleanDatabase.py file to access your MySQL using your mySQL account information.

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

######FINISHED HERE 3/19/18 continue here

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

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
