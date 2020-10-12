FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user/app/

# Install system dependencies
RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    python3 -m pip install --no-cache-dir pip-tools

# install python dependencies



# create the appropriate directories
ENV HOME=/home/user/app/
ENV APP_HOME=/home/user/app/
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/staticfiles
#WORKDIR $APP_HOME

# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm /var/lib/apt/lists/* rm -rf /var/cache/apt/*

ADD . /home/user/app/

RUN pip install -r requirements.txt

USER user
CMD gunicorn visportAPI.wsgi --log-file - -b 0.0.0.0:9000 --reload
