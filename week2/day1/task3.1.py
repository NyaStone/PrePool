def functionA(someString: str, someNum: int):
    lowercaseLetters = list(filter(str.islower, someString))
    return len(lowercaseLetters) >= someNum

def functionB(someString: str, someNum: int):
    lowercaseLetters = list(filter(str.isupper, someString))
    return len(lowercaseLetters) >= someNum

def functionC(someString: str, someNum: int):
    return len(someString) >= someNum

def functionD(someString: str, someNum: int):
    alphanumericalCharacters = list(filter(str.isalnum, someString))
    return len(someString) - len(alphanumericalCharacters) >= someNum

def functionE(someString: str, someNum: int):
    numberChars = list(filter(str.isdigit, someString))
    return len(numberChars) >= someNum


# example usage generated using GPT

# Example 1: Simple password-like string
s1 = "Password123!"

# Example 2: Mostly lowercase
s2 = "thisisaverysimpleexample"

# Example 3: Mix of uppercase, digits, and special characters
s3 = "HELLO_WORLD_12345!!"

# Example 4: No special characters, only letters and numbers
s4 = "JustSomeTextAnd123Numbers"

# Example 5: Short string with digits and special characters
s5 = "Ab#12"

# Testing funA
print(functionA(s1, 2))  
print(functionA(s2, 10)) 

# Testing funB
print(functionB(s3, 5)) 
print(functionB(s4, 3)) 

# Testing funC
print(functionC(s5, 6))  
print(functionC(s4, 5))  

# Testing funD
print(functionD(s1, 1))  
print(functionD(s4, 2))  

# Testing funE
print(functionE(s3, 5)) 
print(functionE(s2, 1)) 
