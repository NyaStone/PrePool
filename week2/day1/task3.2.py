from typing import Callable

def lower(someString: str, someNum: int):
    lowercaseLetters = list(filter(str.islower, someString))
    return len(lowercaseLetters) >= someNum

def upper(someString: str, someNum: int):
    lowercaseLetters = list(filter(str.isupper, someString))
    return len(lowercaseLetters) >= someNum

def count(someString: str, someNum: int):
    return len(someString) >= someNum

def special(someString: str, someNum: int):
    alphanumericalCharacters = list(filter(str.isalnum, someString))
    return len(someString) - len(alphanumericalCharacters) >= someNum

def digit(someString: str, someNum: int):
    numberChars = list(filter(str.isdigit, someString))
    return len(numberChars) >= someNum


def checkPassword(checker: Callable[[str, int], bool], count: int, password: str):
    if count <= 0: 
        raise Exception("Invalid count for a ckecker")
    return checker(password, count)





def isSecure(someString: str):
    if not checkPassword(count, 12, someString):
        raise Exception("The password is too short")
    if not checkPassword(lower, 1, someString):
        raise Exception("No lower character found")
    if not checkPassword(upper, 1, someString):
        raise Exception("No upper character found")
    if not checkPassword(special, 1, someString):
        raise Exception("No special character found")
    if not checkPassword(digit, 1, someString):
        raise Exception("No digit character found")
    
try:
    isSecure(input("Password? "))
    print("The password is fine")
except Exception as e:
    print(e)