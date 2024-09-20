import unicodedata


def normalize(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    res = u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return ''.join(filter(str.isalpha, res)).lower()


def recursiveChecker(someString: str): 
    if len(someString) <= 1:
        return True
    return someString[0] == someString[len(someString) -1 ] and recursiveChecker(someString[1:len(someString)-1])

kayak = normalize("kayak")
oddeven = normalize("never odd or even")
carcat = normalize("Was it a car or a cat I saw?")
gaylord = normalize("gaylord")
print(f'"{kayak}" is {"" if recursiveChecker(kayak) else "not "}a palindrome')
print(f'"{oddeven}" is {"" if recursiveChecker(oddeven) else "not "}a palindrome')
print(f'"{carcat}" is {"" if recursiveChecker(carcat) else "not "}a palindrome')
print(f'"{gaylord}" is {"" if recursiveChecker(gaylord) else "not "}a palindrome')