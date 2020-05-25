# win-task-scheduler

Windows Task Scheduler comes pre-installed on most windows installations

It is a "simple" application that lets you run scheduled tasks (once or on a repeated basis), similar to cron

https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page

It doesn't have complex resource logic or event chaining, but it is a n easy way to get something scheduled to run at 1am so you can go to sleep and not stay up to press buttons.

It can be used through the GUI provided by windows, and it is good to be familiar with it as this will most likely be the way to debug your scripts if they fail, but it can also be invoked programmatically.

The follow example shows how:

------------

    ├── demo.py           <- Simple demo app that writes current time in demo.txt in python
    ├── demo.bat          <- Activates the default miniconda enviroment (or one of your choosing)
    ├── schedule.py       <-- Schedules demo.py to run 30 seconds in the future.
    ├── demo.R            <- Simple demo app that writes current time in demo.R.txt in R 
    └── schedule.R        <- Schedules demo.R to run 30 seconds in the future.
    
   
--------
