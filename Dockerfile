# pull official base image
FROM python:3.8.9-slim

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/entrypoint.sh

# copy project
COPY . /usr/src/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]