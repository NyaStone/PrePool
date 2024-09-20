import unicodedata
from collections import defaultdict
from math import gcd
from functools import reduce


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

def find_repeated_sequences(ciphertext, length=4):
    repeats = defaultdict(list)
    
    # Find sequences of the given length
    for i in range(len(ciphertext) - length):
        sequence = ciphertext[i:i+length]
        # Store positions of the sequence
        for j in range(i + length, len(ciphertext) - length):
            if ciphertext[j:j+length] == sequence:
                repeats[sequence].append(j - i)
    
    return repeats

def kasiski_test(ciphertext, repeatLenth):
    ciphertext = normalize(ciphertext)
    repeats = find_repeated_sequences(ciphertext, repeatLenth)
    distances = []
    for seq, positions in repeats.items():
        if len(positions) > 1:
            # Add distances for this sequence
            distances.extend(positions)
    if distances:
        return find_gcd_of_distances(distances)
    else:
        return None

def find_gcd_of_distances(distances):
    return reduce(gcd, distances)

def index_of_coincidence(text):
    N = len(text)
    frequencies = [text.count(chr(i)) for i in range(65, 91)]  # A-Z frequencies
    
    IC = sum(f * (f - 1) for f in frequencies) / (N * (N - 1))
    return IC

def friedman_test(ciphertext):
    IC = index_of_coincidence(ciphertext)
    
    # For random text, expected IC is ~0.0385
    # For normal English, expected IC is ~0.068
    
    # Estimated key length based on IC
    expected_IC_random = 0.0385
    expected_IC_english = 0.068
    
    N = len(ciphertext)
    
    # Formula to estimate key length:
    k_est = (expected_IC_english - expected_IC_random) / (IC - expected_IC_random)
    k_est *= N / (N - 1)
    
    return round(k_est)




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
    
def decodeText(someText: str, key: str):
    someText = normalize(someText)
    normedkey = normalize(key)
    key = normedkey
    #repeating the key to be at least as long as the string to encrypt
    while len(key) < len(someText):
        key += normedkey
    decodedString = ""
    for index in range(len(someText)):
        character = someText[index]
        keyCharacter = key[index]
        decodedString += decode(character, keyCharacter)
    return decodedString



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

def deocdeVigenere(someString: str):
    possibleKeyLength = []
    for repeatLength in range(3, 6):
        kasikiValue = kasiski_test(someString, repeatLength)
        if kasikiValue:
            possibleKeyLength.append(kasikiValue)
    friedmanValue = friedman_test(someString)
    if friedmanValue and friedmanValue > 0:
        possibleKeyLength.append(friedmanValue)

    if not possibleKeyLength:
        raise Exception("Couldn't determine the keylength")
    possibleKeyLength = list(dict.fromkeys(possibleKeyLength))

    print(possibleKeyLength)
    # keyLength = kasiski_test(encodedString, 4)
    # print(f'Keylength is: {keyLength}')

    possibleKeys = []
    for keyLength in possibleKeyLength:
        # splitting the encypted text into segments that use the same letter as encription key
        cesarCyphers = []
        for i in range(keyLength):
            cesarCyphers.append("")
        for index, character in enumerate(encodedString):
            cesarCyphers[index % keyLength] += character
        # break each cesar cypher individualy to reconstruct the key
        decypheredKey = ""
        for encrypted in cesarCyphers:
            decypheredKey += decodeCesar(encrypted)
        possibleKeys.append(decypheredKey)

    # try to decrypt the message with each possible key and compare results
    translations = []
    for key in possibleKeys:
        decodedText = decodeText(someString, key)
        frequency = characterFrequency(decodedText)
        score = compareFrequency(frequency)
        translations.append({
            "test": decodedText,
            "score": score,
            "key": key
        })

    # pick the match with the closest score
    bestResult = None
    bestScore = None
    for result in translations:
        if not bestScore:
            bestScore = result["score"]
            bestResult = result
        elif bestScore > result["score"]:
            bestScore = result["score"]
            bestResult = result

    return bestResult




# someString = input("Please enter some text to encrypt:\n")
someString = "Somebody once told meThe world is gonna roll meI ain't the sharpest tool in the shedShe was looking kind of dumbWith her finger and her thumbIn the shape of an L on her foreheadWell, the years start comingAnd they don't stop comingFed to the rules and I hit the ground runningDidn't make sense not to live for funYour brain gets smartBut your head gets dumbSo much to do, so much to seeSo what's wrong with taking the back streets?You'll never know if you don't goYou'll never shine if you don't glowHey now, you're an all starGet your game on, go playHey now, you're a rock starGet the show on, get paidAnd all that glitters is goldOnly shooting stars break the moldIt's a cool place and they say it gets colderYou're bundled up nowBut wait till you get olderBut the meteor men beg to differJudging by the hole in the satellite pictureThe ice we skate is getting pretty thinThe water is getting warmSo you might as well swimMy world's on fire, how about yours?That's the way I like itAnd I never get boredHey now, you're an all starGet your game on, go playHey now, you're a rock starGet the show on, get paidAnd all that glitters is goldOnly shooting stars break the moldHey now, you're an all starGet your game on, go playHey now, you're a rock starGet the show on, get paidAnd all that glitters is goldOnly shooting starsSomebody once askedCould I spare some change for gas?I need to get myself away from this placeI said: Yep, what a conceptI could use a little fuel myselfAnd we could all use a little changeWell the years start comingAnd they don't stop comingFed to the rules and I hit the ground runningDidn't make sense not to live for funYour brain gets smartBut your head gets dumbSo much to do, so much to seeSo what's wrong with taking the back streetsYou'll never know if you don't go (go!)You'll never shine if you don't glowHey now, you're an all starGet your game on, go playHey now, you're a rock starGet the show on, get paidAnd all that glitters is goldOnly shooting stars break the moldAnd all that glitters is goldOnly shooting stars break the mold"
# someString = "Somebody once told meThe world is gonna roll meI ain't the sharpest tool in the shedShe was looking kind of dumbWith her finger and her thumbIn the shape of an L on her forehead"
normalisedString = normalize(someString)
someKey = input('Please enter a passphrase as key:\n')
key = normalize(someKey)
#repeating the key to be at least as long as the string to encrypt
while len(key) < len(someString):
    key += someKey

encodedString = ""

for index in range(len(normalisedString)):
    character = normalisedString[index]
    keyCharacter = key[index]
    encodedString += encode(character, keyCharacter)

print(encodedString)


decypheredKey = deocdeVigenere(encodedString)


print(f'I guess the key was "{decypheredKey}"')