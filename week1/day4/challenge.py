import re
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

someNumber = ""
someString = input('Enter some text: ')

while not someNumber.isdigit():
    someNumber = input('Enter a number: ')
    if not someNumber.isdigit():
        print(f'"{someNumber}" is not an integer')
someNumber = int(someNumber)

if someNumber == 0:
    exit()


if someNumber >= 42 or re.match(r'[aeiouy]', remove_accents(someString).lower()) != None:
    print(f'The number was {someNumber}')
else:
    print(f'The string was "{someString}"')