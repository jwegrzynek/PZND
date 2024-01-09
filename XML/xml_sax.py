from xml.sax import parse, SAXException
from xml.sax.handler import ContentHandler


class DictHandler(ContentHandler):
    """Turns XML into dictionary"""

    def __init__(self):
        super().__init__()
        self.element_stack = []

    @property
    def current_element(self):
        return self.element_stack[-1]

    # Called when start element is found
    def startElement(self, name, attrs):
        self.element_stack.append({'name': name,
                                   'attributes': dict(attrs),
                                   'children': [],
                                   'value': ''
                                   })

    # Called when end element is found
    def endElement(self, name):
        if len(self.element_stack) > 1:  # Checking if there are some children
            child = self.element_stack.pop()
            self.current_element['children'].append(child)

    # Called when character is found
    def characters(self, content):
        self.current_element['value'] = content


handler = DictHandler()
parse('protein_P01024.xml', handler)
root = handler.current_element


# print(root['children'][0])


# Zadanie 3

class FinishedParsing(SAXException):
    pass


class ProteinNameHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self.in_fullname = False
        self.fullname = ""
        self.found_first_fullname = False

    def startElement(self, name, attrs):
        if name == "fullName" and not self.found_first_fullname:
            self.in_fullname = True

    def endElement(self, name):
        if name == "fullName" and not self.found_first_fullname:
            self.in_fullname = False
            self.found_first_fullname = True

    def characters(self, content):
        if self.in_fullname:
            self.fullname = content.strip()
            raise FinishedParsing('ParsingEnded')


handler = ProteinNameHandler()
try:
    parse('protein_P01024.xml', handler)
except FinishedParsing:
    pass

root = handler.fullname
print(root)
