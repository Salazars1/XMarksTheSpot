#!/usr/bin/env python
import os
import sys
import sched
import time
import datetime
from functools import wraps
from threading import Thread
from datetime import datetime

#threading done here to execute every second
#@source https://stackoverflow.com/questions/2398661/schedule-a-repeating-event-in-python-3
def async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl
    return async_func

def schedule(interval):
    def decorator(func):
        def periodic(scheduler, interval, action, actionargs=()):
            scheduler.enter(interval, 1, periodic,
                            (scheduler, interval, action, actionargs))
            action(*actionargs)

        @wraps(func)
        def wrap(*args, **kwargs):
            scheduler = sched.scheduler(time.time, time.sleep)
            periodic(scheduler, interval, func)
            scheduler.run()
        return wrap
    return decorator


@async
@schedule(1)
def periodic_event( ): #run the periodic event
    if checkIfMidnight() == True: #check that it's midnight
        os.system("python resetReservationsDaily.py")

#function to check how long it's been since midnight, if its midnight, difference is 0
#@source https://stackoverflow.com/questions/40118869/python-how-to-check-if-time-is-midnight-and-not-display-time-if-true
def checkIfMidnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_since_midnight = (now - midnight).total_seconds()
    print (seconds_since_midnight) # print seconds since it was midnight
    if (seconds_since_midnight < 2):
        return True
    else:
        return False

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "XMarksTheSpot.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    periodic_event() #running in the backend every second
    execute_from_command_line(sys.argv)
