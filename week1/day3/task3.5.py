someString = "This is a test. Is it possible to fly? Good things come to those who never give up."


def normalizePunctuation(fstring: str):
    normalizedString = fstring.replace("?", ".")
    normalizedString = normalizedString.replace("!", ".")
    return normalizedString

def splitSentences(fstring: str):
    normalizedString = normalizePunctuation(fstring)
    return normalizedString.split(". ")

def grabFirstWord(fstring: str):
    words = fstring.split(' ')
    return words[0].lower()

def task(fstring: str):
    res = ""
    sentences = splitSentences(fstring)
    for sentence in sentences:
        res += f'{grabFirstWord(sentence)} '
    res = f'{res[:-1]}.'
    return res.capitalize()
        
print(task(someString))
