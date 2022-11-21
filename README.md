# IC2 project 
The aim of this project is to explore the **ImageTragick** exploits. These exploits were demostrated on a simple web app written in Node.js utilizing the ImageMagick library. 
## MagickShell
MagickShell is something like a reverse shell which communicates with the web app through HTTP POST and GET utilizing some of the exploits.
Magick shell can be run from the terminal as follows `pipenv run python magick_shell.py`. 
The programs dependencies are all included in the Pipfile. Dependencies can be installed by running the command `pipenv shell` and then `pipenv install`.
## Project dependencies
- Docker
- docker-compose
- Node.js v6.1.0
- npm
- pipenv
