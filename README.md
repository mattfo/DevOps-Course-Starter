# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
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



Matt extra notes:

I've done everything above - I Got poetry run flask run - working

Need to run:

% poetry add requests


this added the line
requests = "^2.25.1"
to pyproject.toml

Need to set up a Trello Account and update your credentials for KEY and TOKEN in config.py

There are other uppercarse variables set up in there, you can add those as you become aware of what they are, for instance you will need to create a board before using BOARD

BOARD = '60aae4dd3a59791541c8dc93'
BOARDTEXT = "Matts ToDo Board"

List: TODO = "60aae5fbefcb672f2976a218"
Task: PYTHONWORK = "60aae7d9d819b725a1df6c91"

List: DOING = "60aae600b685fb7eeda92576"
Task: JSONWORK	= "60aae7e68ae1e01db6226b86"

List: DONE = "60aae6034a30146398a55e17"
Task: POSTMANWORK = "60aae7eeb7863687b3ca0d2c"

Refer to useful documents:

https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-get
https://docs.python-requests.org/en/master/user/quickstart/#make-a-request

The exercise involves:

F • Fetch all to-do items (cards) for the specified board
I • Create a new card on the board's 'To Do' list
H • Move a card from 'To Do' to 'Done' (or 'Doing' if you want to allow in-progress to-do items)