from xml.dom.minidom import parse, parseString
import pandas as pd
# Downloading data
import requests
from functools import lru_cache

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

# print(sum(df['id'].isna()))

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


get_protein_name(file_path)


# def get_protein_name(document):
#     first_full_name = document.getElementsByTagName('fullName')[0]
#     return first_full_name.firstChild.wholeText


def get_protein_xml(id):
    url = f'https://www.uniprot.org/uniprotkb/{id}.xml'
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Invalid status code for id={id}')
        return

    return parseString(response.text)


@lru_cache
def get_protein_name_by_id(id):
    """Returns protein name of a protein defined with Uniprot id"""

    if (dom := get_protein_xml(id)) is not None:
        return (dom.getElementsByTagName('protein')[0]
                .getElementsByTagName('recommendedName')[0]
                .getElementsByTagName('fullName')[0]
                .firstChild.nodeValue)


print(get_protein_xml('P98160'))
print(get_protein_name_by_id('P98160'))

proteins_names = [get_protein_name_by_id(id) for id in df['id']]

print(proteins_names)

df.id.apply(get_protein_name_by_id)




