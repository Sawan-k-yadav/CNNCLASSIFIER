# for automating the process of creating environment variable
# It is shell script which runs in linux kernel

echo [$(date)]: "START"   # echo used for giving some message
echo [$(date)]: "creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment"  # As I had one error firstly while activating the environement 
source activate ./env                         # because in pyproject.toml I had written ture inplace of true
echo [$(date)]: "installing the dev requirements"   # SO we can then run activate command only after correcting
pip install -r requirements_dev.txt                 # the code.
echo [$(date)]: "END"
