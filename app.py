from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
from housing.entity.config_entity import DataIngestionConfig
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    logging.info(f"we are testing logging module {DataIngestionConfig}")
    try:
        # pipeline = Pipeline(config=Configuration())
        # pipeline.run_pipeline()
        logging.info(f"Works fine")
    except Exception as e:
        logging.info(HousingException(e, sys))
    return "Starting Machine learning project"


if __name__ == "__main__":
    app.run(debug = True)