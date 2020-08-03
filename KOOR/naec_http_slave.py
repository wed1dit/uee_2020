import requests
import time
from bs4 import BeautifulSoup as BS
import os
import shutil

proto = 'http://'
host = 'localhost'
port = 55001

url = f"{proto}{host}:{port}"

response = requests.get(url)
soup = BS(response.content, 'html.parser')

all_url = list(filter(lambda c: c.endswith('.pdf'),
                      [c.get_text() for c in soup.findAll('a')]))


def download(directory_to='maindir'):
    base_dir = os.getcwd()
    path_to_maindir = os.path.join(base_dir, directory_to)
    try:
        shutil.rmtree(path_to_maindir)
    except FileNotFoundError:
        pass
    if not os.path.isdir(directory_to):
        os.mkdir(directory_to)
    os.chdir(path_to_maindir)
    for each in all_url:
        whole_url = url + f'/{each}'
        pdf_content = requests.get(whole_url)
        with open(each, 'wb') as fp:
            fp.write(pdf_content.content)
    os.chdir(base_dir)
            

download()