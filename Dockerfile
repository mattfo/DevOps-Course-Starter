FROM python:3.7.11 as base 
# Perform common operations, dependency installation etc... 

# Download and install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH $PATH:/root/.poetry/bin

# Copy current direcotry to docker container I think
COPY . . 

# Install dependencies
RUN /root/.poetry/bin/poetry install

# Run the flask web server (on docker run)
ENTRYPOINT /root/.poetry/bin/poetry run flask run





# To run the above from command line port 5000 to 5000:
# $ docker run --env-file .env -p 5000:5000 todo-app 
# It doesn't work though