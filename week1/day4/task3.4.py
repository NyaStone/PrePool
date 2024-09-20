import unicodedata

english = "etaoinsrhldcumfpgwybvkxjqz"


def normalize(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    res = u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return ''.join(filter(str.isalpha, res))

def encode(character: str, key: str):
    if len(character) != 1:
        raise Exception(f'"{character}" is not a single character')
    if len(key) != 1:
        raise Exception(f'"{key}" is not a single character')
    characterValue = ord(character[0].upper())-65
    keyValue = ord(key[0].upper())-65
    encodedCharacterValue = (characterValue + keyValue) % 26
    return chr(encodedCharacterValue + 65)

def decode(character: str, key: str):
    if len(character) != 1:
        raise Exception(f'"{character}" is not a single character')
    if len(key) != 1:
        raise Exception(f'"{key}" is not a single character')
    characterValue = ord(character[0].upper())-65
    keyValue = ord(key[0].upper())-65
    encodedCharacterValue = (characterValue - keyValue) % 26
    return chr(encodedCharacterValue + 65)


someString = input("Please enter some text to decrypt:\n")
normalizedString = normalize(someString)

keyLength = ""

while not keyLength.isdigit():
    keyLength = input('Enter the guessed keylength: ')
    if not keyLength.isdigit():
        print(f'"{keyLength}" is not an integer')
keyLength = int(keyLength)

substrings = []


# splitting the code in keylength parts
for i in range(0, len(normalizedString), keyLength):
    substrings.append(normalizedString[i:i+keyLength])


# collect all letter suposedly using the same encryption letter
keyEncodings = []
for i in range(keyLength):
    keyEncodings.append("")
    for substring in substrings:
        if i < len(substring): 
            keyEncodings[i] += substring[i]

# conduct frequency analysis 
characterFrequencies = []
for haveSameKey in keyEncodings:
    characterCounts = {}
    for character in haveSameKey:
        upperCharacter = character.upper()
        if upperCharacter.isalpha():   
            if not upperCharacter in characterCounts:
                characterCounts[upperCharacter] = 0
            characterCounts[upperCharacter] += 1
    characterFrequencies.append(characterCounts)

# compare the frequencies of the characters and average out the offset 
for letters in characterFrequencies:
    frequencyFingerprint = ""
    for letter,val in sorted(letters.items(), key=lambda kv: kv[1], reverse=True):
        frequencyFingerprint += letter
        
    encryptedLetter = ord(frequencyFingerprint[0])-65
    assumedLetter = ord(english[0])-65
    offset = (encryptedLetter - assumedLetter) % 26
    assumedOrigialKey = chr(offset+65)
    print(assumedOrigialKey)

print(characterFrequencies)