from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
def main():
    try:
        pipeline = Pipeline(config=Configuration())
        pipeline.run_pipeline()
        # print(Configuration().get_data_transformation_config())
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()