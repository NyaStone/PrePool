import unicodedata
import numpy as np
import Levenshtein

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def normalizeSrting(someString):
    replacedAccents = remove_accents(someString)
    res = ""
    for character in replacedAccents.upper():
        if character.isalpha():
            res += character
    return res


def encode(character: str, key: int):
    if len(character) != 1:
        raise Exception(f'"{character}" is not a single character')
    characterValue = ord(character[0].upper())-65
    encodedCharacterValue = (characterValue + key) % 26
    return chr(encodedCharacterValue + 65)

def characterFrequencyFingerprint(someString: str):
    frequencies = {}
    for character in someString:
        if not character in frequencies:
            frequencies[character] = 0
        frequencies[character] += 1
    frequencyFingerprint = ""
    for letter in sorted(frequencies.items(), key=lambda kv: kv[1], reverse=True):
        frequencyFingerprint += letter[0]
    return frequencyFingerprint
 


def decode(someString: str):
    # generate the 26 possiblities of decoding
    possibleSolutions = []
    for i in range(26):
        maybeSolution = ""
        for character in someString:
            maybeSolution += encode(character, i)

        fingerprint = characterFrequencyFingerprint(maybeSolution)
        possibleSolutions.append({
            "solution": maybeSolution,
            "fingerprint": fingerprint,
            "score": Levenshtein.distance(fingerprint, english)
        })
    possibleSolutions.sort(key= lambda solution: solution["score"])
    
    for solution in possibleSolutions:
        print(solution["solution"])
        input()


someString = input("Please enter some text to decrypt:\n")

decode(normalizeSrting(someString))