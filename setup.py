from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "ML project speed run"
VERSION = "0.0.1"
AUTHOR = "Prakashmani Awasthi"
DESCRIPTION = "A practice speed run for full stack ML project"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: this function is made to return the list of requirements
    mentioned in the requirement.txt file

    the list returned contains names of all the libraries mentioned in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        return requirements_list

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author = AUTHOR,
    description= DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)