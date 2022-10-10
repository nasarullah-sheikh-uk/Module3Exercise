# Immutable infrastructure
For production isntance of application please add gunicorn in dependencies. Running
> poetry add gunicorn 
in base local folder will add the dependency to the poetry file. A poetry install will then later install the gunicorn as well

To copy unnecessary files please create a .dockerignore and fill it with all names of files/folders not to be copied into images, e.g.:
==========================
.env.template
.github
.venv
.vscode
Ansible
Tests
.gitpod.yml
.gitignore
.dockerignore
.env.test
.git
Dockerfile
==========================

To build base images, go to base of the project which contains the Dockerfile and run

> docker build --target development --tag todo-app:dev .
> docker build --target production --tag todo-app:prod .

This will build the images for Dev and Prod environments. These are roughly 140MB each.

To start the Production docker listening at 8080 on host :
> docker run --env-file .env -d -p 8080:5000 --name myappP todo-app:prod

========================================
.env file contains
# Flask server configuration.
FLASK_APP=todo_app/app
FLASK_ENV=development
SECRET_KEY=
URL=https://api.trello.com/
APIKEY=<>
APIToken=<>
TrelloBID=<>
============================================

Check the docker is up by checking "docker ps" or "docker logs myappP" or just access the webpage 127.0.0.1:8080

Start a shell in the running docker to check:
>docker exec -it myappP /bin/sh
1) There are no unnecessary files there ( cd /app; ls -a ; ls -a todo_app)
2) run top and you will see the gunicorn running

To start the Developement docker listening at 8088 (differnt ports just incase u run both containers on same host for checks at same time) on host :
> set PWD="PATH to root folder of project"
e.g
> set PWD="C:\Users\nasar\Documents\GitHub\Module3Exercise"
> docker run --env-file .env -d -p 8088:5000 --mount type=bind,source="%PWD%"/todo_app,target=/app/todo_app --name myappD todo-app:dev

Check the docker is up by checking "docker ps" or "docker logs myappD" or just access the webpage 127.0.0.1:8088
Please note here any change in code will result a change in docker mounted volume and will be changed on web dynamically.

# Ansible
There is a Ansible folder which has 
.env.j2, inventory_file, play_file and todoapp.service files

These need to be copied to Ansible control node, so that the Playbook play_file uses the depndencies at run time.

Step1 - Copy all these files to control node /some/path
Step2 - Change the references to path in play_file for source
Step3 - Run the Command -- > #  ansible-playbook /path/play_file -i /path/inventory_file
this will ask :
    What is the api key?: <enter yours>
    What is the api token?: <enter yours>
    What is the trellobid?: <enter yours>
Step4 - Check on managed nodes that the webserver is listening on the 5000 port ( netstan -an | grep <port>)
Step5 - Check the logs on managed node -  journalctl -u todoapp

# Testing
There are three unit tests in Tests folder to check the filtering of items/cards happens by Status. There is a seperate test for each status
On terminal run
> pytest -s 
This will show if the filtering passes
For individual test
> pytest test_name -s

To check which tests are runnable run
> pytest --collect-only

There is a integeration test with a stub named test_client.y which checks the returned html for O/p- for an API of get cards
It asserts the names of cards.

# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```
It will add the `poetry` command to Poetry's bin directory, generally located at: C:\Users\<USER>\AppData\Roaming\Python\Scripts

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.
There are four varaibles for trello access
APIKEY
APIToken
TrelloBID
URL = "https://api.trello.com/"
These should be added to the env file to access Trello boards


## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.
