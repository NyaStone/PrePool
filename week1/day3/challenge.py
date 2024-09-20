def countOccurences(fstring: str, fword: str):
    invertedString = fstring[::-1]
    stringlength = len(fstring)
    wordlength = len(fword)
    lowerword = fword.lower()
    count = 0
    for i in range(stringlength-wordlength+1):
        substring = fstring[i:i+wordlength].lower()
        invertedSubstring = invertedString[i:i+wordlength].lower()
        if substring == lowerword or invertedSubstring == lowerword:
            count += 1
    return count
    
someString = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
occurences = countOccurences(someString, 'Cat') + countOccurences(someString, 'Mice') + countOccurences(someString, 'Garden')

print(f'{occurences} occurences of Cat, Mice, Garden or their reverse in "{someString}"')

