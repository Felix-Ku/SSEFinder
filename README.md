# COMP3297-SSEFinder
COMP3297 Group F Project

Project: 
COMP3297 Pre-project

Author: 
Ku Sze Hung, Felix 

UID: 
3035370363

Structure:
Config_folder = CovidData
App = CovidDataPortal

Testing: 
Successfull in local and online production environment

To run in local:
Modify the Settings.py
	1. Database settings
	2. Remove env() stuffs


To add new pages:
    1. Add new template pages inside \templates\
    2. Create function for the new page into \Portal\views.py
    3. Add new function and page info into \Portal\urls.py
    4. Create links in base.html
