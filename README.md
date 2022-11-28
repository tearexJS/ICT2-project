# IC2 project 
The aim of this project is to explore the **ImageTragick** exploits. These exploits were demostrated on a simple web app written in Node.js utilizing the ImageMagick library. 
## MagickShell
MagickShell is something like a reverse shell which communicates with the web app through HTTP POST and GET utilizing some of the exploits.
Magick shell can be run from the terminal as follows `pipenv run python magick_shell.py`. 
## Web app
Simple web app utilizing the ImageMagick lib to convert images to png format. The web app can be run as following `npm run docker:dev`
## Installation
For successful installation check **Project dependencies**.
### Web app
To successfuly make the web app work you have to run the following commands:
- `npm install` in the `ICT2-project/magick-app` folder
- `npm run docker:dev-build`
### MagickShell
To make the **MagickShell** work you have to run the following commands 
- `pipenv install` in the `ICT2-project/magick-shell` folder
The programs dependencies are all included in the Pipfile. Dependencies can be installed by running the command `pipenv shell` and then `pipenv install`.
## Project dependencies
- Docker
- docker-compose
- Node.js v6.1.0
- npm
- pipenv
