from collections import namedtuple

DataIngetionConfig=namedtuple("DataIngestionConfig",
["data_download_url", "tgz_download_dir", "raw_data_dir", "ingested_train_dir", "ingested_test_dir"])


TrainingPipelineConfg = namedtuple("TrainingPipelineConfig", 
["artifact_dir"])