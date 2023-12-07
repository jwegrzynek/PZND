# Downloading data
import requests

url = 'https://www.uniprot.org/uniprotkb/P01024.xml'
response = requests.get(url)

with open('protein_P01024.xml', 'w') as f:
    f.write(response.text)

from xml.dom.minidom import parse, parseString, Node


def get_all_tags(elem):
    """Returns set of all tags in the element"""

