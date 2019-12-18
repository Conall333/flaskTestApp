<h2>Notes</h2>

* Setup
    * to create virtual enviroment `virtualenv -p python3 venv` 
    * To activate virtual Environment:`source bin/activate` --> when in virtual env directory   
    * To install Flask: `pip3 install flask`  
    * To run the server: `export FLASK_APP=server.py`
    `python3 -m flask run`  
    * To change production environment to development:
    `export FLASK_ENV=development`
    
* Flask
    * render_template() will look for files in a templates directory
    * css and js should be in static folder
    * Flask uses a templating engine anything in {{ }} is evaluated as python
    * Variable Rules
    
* docker-compose.yml
    * `container_name` to define name for each container
    * `restart: unless stopped` -> containers will only be stopped when the docker engine is stopped/restarted
    * `environment` -> contains enviroment variables that are passed to the container
