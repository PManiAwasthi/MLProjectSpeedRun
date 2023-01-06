import os, sys
import pandas as pd
from housing.entity.artifact_entity import DataTransformationArtifact, DataIngestionArtifact, DataValidationArtifact
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            logging.info(f"{'='*20}Data Transformation initiated{'='*20}")
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_aritfact = data_validation_artifact
        except Exception as e:
            raise HousingException(e, sys) from e