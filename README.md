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

# Consumer Behaviour - Dashboard

> This is a single page dashboard for consumer behaviour. It contains an interactive visualisations for the data collected over time on consumer behaviour.
> Live demo [_here_](https://heroku-cb-dash.herokuapp.com/).

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [DevelopmentStage](#Development-stage)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
<!-- * [License](#license) -->

## General Information

> The administration of a well known retail store is interested in using data collected over time from their various branches to understand consumer behaviour in the different regions of the country. Using the data to create interactive visualisations to tell a story about their customers.

> As the data was collected over 10 years from all branches, it was inconsistent in terms of format and content. So only after cleaning the data, I was able to use it for this dashboard.

> User Story:-?????
> [_here_](https://miro.com/app/board/uXjVOVHkNlY=/)

## Technologies Used

- Python
- Dash

## Features

List the ready features here:

- View the visualised versiion of data in graphs.

## Screenshots

![User Story]()

## Setup

Project Deliverables

- A cleaned and transformed version of the data provided.
- Interactive visualisation of customer expectations using cleaned data.

Install / setup one's local environment / get started with the project.

- Install via terminal pip3 install dash
- Run the dashoard app python3 app.py

## Development Stage

25/02/22

1. What have you done so far

- Created the file to upload the data collected from all branches.

2. What are you going to work on next

- Create graphs to show visual data, based on customer expectations

3. What blockers you have (if any)

14/03/22

1. What have you done so far

- Created graphs to show visual data, using plotly
- Import plotly and pandas

2. What are you going to work on next

3. What blockers you have (if any)

## Usage

How does one go about using it?

- Can be used via the demo link. This can be done via the deployment url specified in the introduction.

Provide various use cases and code examples here.

- For example, this can be used when trying to find an array of genres:-
  `router.get('/', (req, res) => { Genre.find({}, function (error, genres) { if (error) { res.status(400).json({ message: ({ message: 'Unable to find Genre'}) }); } else { res.status(200).json(genres); } }); });`
- For example, this can be used when trying to find a specific Album by specifing the id e.g https://deploy-isdb.herokuapp.com/albums/2:-
  `router.get('/:AlbumId', (req, res) => { Album.findOne ({ AlbumId: parseInt(req.params.AlbumId) }, function (error, album) { if (error) { res.status(400).json({ message: ({ message: 'Unable to find Album'}) }); } else { res.status(200).json(album); } }); });`

## Project Status

Project is: _in progress_ / _complete_

## Room for Improvement

## Acknowledgements

This project was based on class tutorials

- Introduction to Dash.

Other resources used for the project include : -

- [Dash](https://dash.plotly.com/).

## Contact

Created by [Stanton]() - feel free to contact me!
