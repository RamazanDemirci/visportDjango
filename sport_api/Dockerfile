# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /usr/src/sport_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/sport_api/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
#COPY ./entrypoint.sh /usr/src/sport_api/entrypoint.sh

# copy project
COPY . /usr/src/sport_api/

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/sport_api/entrypoint.sh"]