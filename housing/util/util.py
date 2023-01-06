import yaml
import os, sys
import numpy as np
import pandas as pd
from housing.constant import DATASET_SCHEMA_COLUMN_KEY
import dill

from housing.exception import HousingException

def read_yaml_file(file_path: str)->dict:
    """
    It reads the yaml file and returns it's content.
    file_path: str, is the location of the file to be read
    """
    try:
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array):
    """
    save numpy array data to file
    file_path: str, location of file to save
    array: np.array, the numpy array to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise HousingException(e, sys) from e

def load_numpy_array_data(file_path: str)->np.array:
    """
    Returns the numpy array from file
    file_path:str, location of the file to retrieve data from
    """
    
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e

def save_object(file_path:str, obj):
    """
    save all kinds of objects to the specified file location
    file_path: str, location to save into
    obj: object to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e

def load_object(file_path: str):
    """
    loads the object from the specified file location
    file_path: str, location to load object from
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e

def load_data(file_path:str, schema_file_path: str) -> pd.DataFrame:
    """
    to load the data as pands dataframe and ensure the columns follow specified datatype constraint
    file_path: str, location to load data from
    schema_file_path: str, the file to compare the data with
    """
    try:
        dataset_schema = read_yaml_file(schema_file_path)

        schema = dataset_schema[DATASET_SCHEMA_COLUMN_KEY]

        dataframe = pd.read_csv(file_path)

        error_message = ""

        for column in dataframe.columnns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message = f"{error_message} \nColumn: [{column}] is not in the schema."
        
        if len(error_message) > 0:
            raise Exception(error_message)
        return dataframe
    except Exception as e:
        raise HousingException(e, sys) from e