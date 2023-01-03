FROM python:3.8.4
COPY . /app
WORKDIR /app
RUN python setup.py install
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app