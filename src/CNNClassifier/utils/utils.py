# Here in utils.py we are those method which we want to use throughout the project

import os
import yaml
from CNNClassifier import logger
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import config_box

@ensure_annotations
def read_yaml(path_to_yaml:Path):
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
        return content



@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass

@ensure_annotations
def load_model():
    pass

@ensure_annotations
def get_size():
    pass

@ensure_annotations
def create_directory():
    pass