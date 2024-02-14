# As this file will be called as soon as we will create object of CNNClassifier
# Thats why we are creating all the logger and other code here

import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_dir="logs"

log_filepath=os.path.join(log_dir, "running_logs.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    formate=logging_str,
    handler=[
        logging.FileHandler(log_filepath),   # This filehandler helps in storing the messages in the file
        logging.StreamHandler(sys.stdout)    # This Streamhandler helps in showing message in 
                                             #   console as well
    ]
)

logger=logging.getLogger("CNNClassifier")