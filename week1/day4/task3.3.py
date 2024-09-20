import unicodedata
import Levenshtein

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
englishFrequency = {
    "E": 0.111607,
    "A": 0.084966,
    "R": 0.075809,
    "I": 0.075448,
    "O": 0.071635,
    "T": 0.069509,
    "N": 0.066544,
    "S": 0.057351,
    "L": 0.054893,
    "C": 0.045388,
    "U": 0.036308,
    "D": 0.033844,
    "P": 0.031671,
    "M": 0.030129,
    "H": 0.030034,
    "G": 0.024705,
    "B": 0.020720,
    "F": 0.018121,
    "Y": 0.017779,
    "W": 0.012899,
    "K": 0.011016,
    "V": 0.010074,
    "X": 0.002902,
    "Z": 0.002722,
    "J": 0.001965,
    "Q": 0.001962
}

def characterRange(startChar: str, endChar: str):
    if len(startChar) != 1:
        raise Exception(f'"{startChar}" is not a single character')
    if len(endChar) != 1:
        raise Exception(f'"{endChar}" is not a single character')
    for ascii in range(ord(startChar), ord(endChar)+1):
        yield chr(ascii)



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

def characterFrequency(someString: str):
    # init the res object with needed keys
    res = {}
    for letter in characterRange("A", "Z"):
        res[letter] = 0
    # count letters
    text = normalize(someString).upper()
    for letter in text:
        res[letter] += 1
    # convert cont to frequency
    for key, value in res.items():
        res[key] = value / len(text)
    return res 

def compareFrequency(textFrequency):
    score = 0
    # After this loop, the lower the score, the closest the match is 
    for letter in characterRange("A", "Z"):
        # absolute value is used to avoid positive and negative distance evening out,
        # and avoiding dealing with negative score
        score += abs(textFrequency[letter] - englishFrequency[letter])
    return score
    
    


# def characterFrequencyFingerprint(someString: str):
#     frequencies = {}
#     for character in someString:
#         if not character in frequencies:
#             frequencies[character] = 0
#         frequencies[character] += 1
#     frequencyFingerprint = ""
#     for letter in sorted(frequencies.items(), key=lambda kv: kv[1], reverse=True):
#         frequencyFingerprint += letter[0]
#     return frequencyFingerprint

def decodeCesar(someString: str):
    # generate the 26 possiblities of decoding
    possibleSolutions = []
    for possibleKey in characterRange("A", "Z"):
        maybeSolution = ""
        for character in someString:
            maybeSolution += decode(character, possibleKey)

        frequency = characterFrequency(maybeSolution)
        score = compareFrequency(frequency)
        print(f'{possibleKey}: {score}')
        possibleSolutions.append({
            "key": possibleKey,
            "solution": maybeSolution,
            "score": score
        })

    # Find the most fitting solution
    deducedKey = possibleSolutions[0]["key"]
    bestScore = possibleSolutions[0]["score"]
    for index, solution in enumerate(possibleSolutions, start=1):
        if solution["score"] < bestScore:
            bestScore = solution["score"]
            deducedKey = solution["key"]

    return deducedKey

someString = input("Please enter some text to encrypt:\n")
normalisedString = normalize(someString)
someKey = input('Please enter a passphrase as key:\n')
key = normalize(someKey)
keyLength = len(key)
#repeating the key to be at least as long as the string to encrypt
while len(key) < len(someString):
    key += someKey

encodedString = ""

for index in range(len(normalisedString)):
    character = normalisedString[index]
    keyCharacter = key[index]
    encodedString += encode(character, keyCharacter)

print(encodedString)

print(f'Keylength is: {keyLength}')

# splitting the encypted text into segments that use the same letter as encription key
cesarCyphers = []
for i in range(keyLength):
    cesarCyphers.append("")
for index, character in enumerate(encodedString):
    cesarCyphers[index % keyLength] += character
# break each cesar cypher individualy to reconstruct the key
decypheredKey = ""
for encrypted in cesarCyphers:
    print(f"Using the same letter: {encrypted}")
    decypheredKey += decodeCesar(encrypted)


print(f'I guess the key was "{decypheredKey}"')