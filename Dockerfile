FROM python:3.7.11-slim-buster
#ENTRYPOINT ["echo", "Hello Fozz"]
# docker build --tag todo-app .
# docker build -f Dockerfile --tag todo-app .

# docker run -p 8080:80 --mount type=bind,src=$(pwd)/shared_space,dst=/opt/chimera/data todo-app


#(
#    docker build -f Dockerfile.cliapp --tag cliapp-matt .
#docker run --mount type=bind,src=$(pwd)/shared_space,dst=/opt/chimera/data cliapp-matt
#)

# docker run todo-app

 # Download and install poetry
 # need run in dockerfile
 RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Copy across your application code
#?
# Define an entrypoint, and default launch command
#?

