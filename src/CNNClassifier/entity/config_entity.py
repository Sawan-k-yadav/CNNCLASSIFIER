from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)   # we use to immutable class
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_data_file:Path
    unzip_dir:Path