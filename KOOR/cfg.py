import yaml
import os
import sys

def read_yaml(filename='metadata.yaml'):
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            data = yaml.load(fp)
    
        return data
    else:
        print(f"{filename} doesnt exist")

yaml = read_yaml()
