from xml.dom.minidom import parse
import pandas as pd
# Downloading data
import requests

url = 'https://www.uniprot.org/uniprotkb/P01024.xml'
response = requests.get(url)

with open('protein_P01024.xml', 'w') as f:
    f.write(response.text)


def get_all_tags(xml_file_path):
    """Returns set of all tags in the element"""

    dom = parse(xml_file_path)
    all_elements = dom.getElementsByTagName('*')
    unique_tags = set()

    for element in all_elements:
        unique_tags.add(element.tagName)

    tag_list = list(unique_tags)

    return tag_list


file_path = 'protein_P01024.xml'
tags_list = get_all_tags(file_path)

# Zad 2
df = pd.read_csv('proteins.csv')

df['id'] = df["Protein"].str.extract(r'\|([^|]+)\|')

print(sum(df['id'].isna()))

df = df[~df['id'].isna()]


# Zad 3
def get_protein_name(xml_file_path):
    # Find all elements with the tag name 'recommendedName'
    dom = parse(xml_file_path)

    # Get the first <protein> element
    protein_element = dom.getElementsByTagName('protein')[0]

    # Find the first <recommendedName> element under <protein>
    recommended_name_element = protein_element.getElementsByTagName('recommendedName')[0]

    # Find the <fullName> element under the first <recommendedName>
    full_name_element = recommended_name_element.getElementsByTagName('fullName')[0]

    # Print the text content of <fullName>
    print(full_name_element.firstChild.nodeValue)

get_protein_name()

