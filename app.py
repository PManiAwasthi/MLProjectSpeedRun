from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    logging.info("we are testing logging module")
    try:
        raise Exception("This is an custom exception test")
    except Exception as e:
        logging.info(HousingException(e, sys))
    return "Starting Machine learning project"


if __name__ == "__main__":
    app.run(debug = True)