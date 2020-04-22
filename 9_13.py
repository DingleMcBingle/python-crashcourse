from collections import OrderedDict

glossary = OrderedDict()

glossary['boolean'] = 'A simple true or false statement'
glossary['variable'] = 'A term that can take on more than one value.'
glossary['definition'] = 'I can\'t think of any more definitions.'

for word, definition in glossary.items():
    print(word.title())
    print(definition)