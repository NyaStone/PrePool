import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def encode(character: str, key: int):
    if len(character) != 1:
        raise Exception(f'"{character}" is not a single character')
    characterValue = ord(character[0].upper())-65
    encodedCharacterValue = (characterValue + key) % 26
    return chr(encodedCharacterValue + 65)


someString = input("Please enter some text to encrypt:\n")

key = ""

while not key.isdigit():
    key = input('Enter a number for key: ')
    if not key.isdigit():
        print(f'"{key}" is not an integer')
key = int(key)

normalisedString = remove_accents(someString)
encodedString = ""
for character in normalisedString:
    if character.isalpha():
        encodedString += encode(character, key)
    else:
        encodedString += character

print(encodedString)