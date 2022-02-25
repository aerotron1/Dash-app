<!-- the skeloton and repo -->
<!-- deploy app via heroku to avoid  -->

1. gitignore to ignore virtual enviroment file and know what to work with:-
   installed gitignore file and created virtual enviroment using python3 -m venv dashvenv and activate it source dashvenv/bin/activate
2. install dash pip3 install dash
3. pip3 freeze > requirements.txt  
   the virtual enviroment used so the requirement.txt only contains
   whats necessary for the app rather than use everything. Because heroku will carry out installation and avoid uneccessary instalations.
   the freeze should store all the requirements in txt
4. Heroku

- Runtime - check version of python build for https://devcenter.heroku.com/articles/python-support#supported-runtimes so for deployment specifiy python version python-3.9.10 used in runtime.txt file
- Dependencies - wat libraries we require
- Procfile - how we serve the app? useed for heroku specifically

  Ref:

https://docs.python.org/3/tutorial/venv.html
