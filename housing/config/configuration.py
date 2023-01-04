from housing.exception import HousingException
import os, sys
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.entity.config_entity import DataIngetionConfig, TrainingPipelineConfg
from housing.logger import logging

class Configuration:

    def __init__(self, config_file_path:str = CONFIG_FILE_PATH, current_time_stamp:str = CURRENT_TIME_STAMP):
        try:
            self.config_info = read_yaml_file(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngetionConfig:
        pass
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfg:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR, 
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY], 
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfg(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e, sys) from e