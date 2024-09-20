import numpy as np

languagesFrequences = {
    "English": "etaoinsrhldcumfpgwybvkxjqz",
    "Spanish": "eaosrnidlctumpbgyívqóhfzjéáñxúüwk",
    "German": "enisratdhulcgmobwfkzvüpäßjöyqx",
    "French": "esaitnrulodcmpévqfbghjàxèyêzçôùâûîœwkïëüæñ",
    "Italian": "eaionlrtscdupmvghfbqzòàùìéèóykwxjô",
    "Greek": "αοιετσνηυρπκμλωδγχθφβξζψ"
}
characterCounts = {}
someString = "Write a program that counts the frequency of each letter from a given text and infers the language of this very text."
letterTotal = 0
for character in someString:
    lowerCharacter = character.lower()
    if lowerCharacter.isalpha():   
        if not lowerCharacter in characterCounts:
            characterCounts[lowerCharacter] = 0
        characterCounts[lowerCharacter] += 1
        letterTotal += 1

frequencyFingerprint = ""

for key,val in sorted(characterCounts.items(), key=lambda kv: kv[1], reverse=True):
    frequencyFingerprint += key
    print(f'letter: {key} : {val} times ({"%.2f" % (val/letterTotal*100)}%)')

print(f'Frequency fingerprint: {frequencyFingerprint}')

# https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])


languageMatches = {}

for key in languagesFrequences:
    languageMatches[key] = levenshtein(languagesFrequences[key], frequencyFingerprint)

language = max(languageMatches, key=languageMatches.get)

print(f'I guess the sentence to be in: {language}')